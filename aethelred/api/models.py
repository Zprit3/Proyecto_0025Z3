"""
Explicación de los campos

    Jugador:*
        nombre: Nombre del jugador.
        cuerpo: Género del personaje (masculino/femenino).
        clase: Clase del personaje (guerrero, hechicera, etc.).
        nivel: Nivel del jugador.
        experiencia: Puntos de experiencia del jugador.
        vida: Puntos de vida del jugador.
        recurso_principal: Puntos del recurso principal del jugador (furia, maná, etc.).
        recurso_secundario: Puntos del recurso secundario del jugador (energía, resistencia, etc.).
        fuerza, inteligencia, agilidad, percepcion, carisma: Atributos del jugador.
        probabilidad_critico: Probabilidad de realizar un ataque crítico.
        velocidad_ataque: Velocidad de ataque del jugador (alta, media, baja).
    Tarjeta:*
        nombre: Nombre de la tarjeta.
        tipo: Tipo de tarjeta (estadística principal, estadística adicional, recurso, evento).
        nivel: Nivel de la tarjeta (1-8).
        rareza: Rareza de la tarjeta (cobre, hierro, etc.).
        efecto: Descripción del efecto de la tarjeta.
    Inventario:*
        jugador: Jugador que posee la tarjeta.
        tarjeta: Tarjeta en el inventario.
        cantidad: Cantidad de tarjetas de este tipo en el inventario.
    Partida:*
        jugador: Jugador al que pertenece la partida.
        progreso: Información del progreso del jugador en la partida (posición, estado del juego, etc.). Este campo puede ser un texto JSON que almacene datos complejos.
        fecha_guardado: Fecha y hora en que se guardó la partida.

Relaciones entre los modelos

    Un Jugador puede tener múltiples Tarjetas en su Inventario.
    Una Tarjeta puede pertenecer al Inventario de múltiples Jugadores.
    Un Jugador puede tener múltiples Partidas guardadas.
    Una Partida pertenece a un único Jugador.
"""

from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=20, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')])
    clase = models.CharField(max_length=50, choices=[
        ('guerrero', 'Guerrero Valiente'),
        ('hechicera', 'Hechicera Astuta'),
        ('ladron', 'Ladrón Escurridizo'),
        ('explorador', 'Explorador Ingenioso'),
        ('bardo', 'Bardo Carismático')
    ])
    nivel = models.IntegerField(default=1)  # Nivel del jugador
    experiencia = models.IntegerField(default=0)  # Experiencia del jugador
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
    rareza = models.CharField(max_length=50, choices=[
        ('cobre', 'Cobre'),
        ('hierro', 'Hierro'),
        ('plata', 'Plata'),
        ('oro', 'Oro'),
        ('platino', 'Platino'),
        ('mithril', 'Mithril'),
        ('orichalcum', 'Orichalcum'),
        ('adamantita', 'Adamantita')
    ])
    efecto = models.TextField()  # Descripción del efecto de la tarjeta

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    class Meta:
        unique_together = ('jugador', 'tarjeta')  # Evita duplicados en el inventario

class Partida(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    progreso = models.TextField()  # Información de la partida (posición, estado del juego, etc.)
    fecha_guardado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Partida de {self.jugador.nombre} ({self.fecha_guardado})"
    
    