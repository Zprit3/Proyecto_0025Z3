from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import JSONField

CLASES = [
    ('guerrero', 'Guerrero Valiente'),
    ('hechicera', 'Hechicera Astuta'),
    ('ladron', 'Ladrón Escurridizo'),
    ('explorador', 'Explorador Ingenioso'),
    ('bardo', 'Bardo Carismático')
]

RAREZAS = [
    ('cobre', 'Cobre'),
    ('hierro', 'Hierro'),
    ('plata', 'Plata'),
    ('oro', 'Oro'),
    ('platino', 'Platino'),
    ('mithril', 'Mithril'),
    ('orichalcum', 'Orichalcum'),
    ('adamantita', 'Adamantita')
]

class Jugador(models.Model):
    nombre = models.CharField(max_length=50, db_index=True)
    cuerpo = models.CharField(max_length=20, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')])
    clase = models.CharField(max_length=50, choices=CLASES)
    nivel = models.IntegerField(default=1)
    experiencia = models.IntegerField(default=0)
    vida = models.IntegerField()
    recurso_principal = models.IntegerField()
    recurso_secundario = models.IntegerField()
    fuerza = models.IntegerField(default=10)
    inteligencia = models.IntegerField(default=10)
    agilidad = models.IntegerField(default=10)
    percepcion = models.IntegerField(default=10)
    carisma = models.IntegerField(default=10)
    probabilidad_critico = models.FloatField(default=0.0)
    velocidad_ataque = models.CharField(max_length=20, choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')])

    def poder_total(self):
        return self.fuerza + self.inteligencia + self.agilidad + self.percepcion + self.carisma

    def __str__(self):
        return self.nombre

class Tarjeta(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=[
        ('estadistica_principal', 'Estadística Principal'),
        ('estadistica_adicional', 'Estadística Adicional'),
        ('recurso', 'Recurso'),
        ('evento', 'Evento')
    ])
    nivel = models.IntegerField()
    rareza = models.CharField(max_length=50, choices=RAREZAS)
    efecto = models.TextField()

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='inventarios')
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE, related_name='inventarios')
    cantidad = models.IntegerField(default=1)

    class Meta:
        unique_together = ('jugador', 'tarjeta')

    def clean(self):
        if self.cantidad < 0:
            raise ValidationError("La cantidad no puede ser negativa.")

    def agregar_tarjeta(self, cantidad=1):
        self.cantidad += cantidad
        self.save()

    def quitar_tarjeta(self, cantidad=1):
        if self.cantidad - cantidad < 0:
            raise ValidationError("No hay suficientes tarjetas en el inventario.")
        self.cantidad -= cantidad
        self.save()

class Partida(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='partidas')
    progreso = JSONField()
    fecha_guardado = models.DateTimeField(auto_now_add=True)

    def actualizar_progreso(self, nuevo_progreso):
        self.progreso = nuevo_progreso
        self.save()

    def __str__(self):
        return f"Partida de {self.jugador.nombre} ({self.fecha_guardado})"