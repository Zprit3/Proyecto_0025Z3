# Generated by Django 5.1.6 on 2025-02-18 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], max_length=20)),
                ('clase', models.CharField(choices=[('guerrero', 'Guerrero Valiente'), ('hechicera', 'Hechicera Astuta'), ('ladron', 'Ladrón Escurridizo'), ('explorador', 'Explorador Ingenioso'), ('bardo', 'Bardo Carismático')], max_length=50)),
                ('nivel', models.IntegerField(default=1)),
                ('experiencia', models.IntegerField(default=0)),
                ('vida', models.IntegerField()),
                ('recurso_principal', models.IntegerField()),
                ('recurso_secundario', models.IntegerField()),
                ('fuerza', models.IntegerField(default=10)),
                ('inteligencia', models.IntegerField(default=10)),
                ('agilidad', models.IntegerField(default=10)),
                ('percepcion', models.IntegerField(default=10)),
                ('carisma', models.IntegerField(default=10)),
                ('probabilidad_critico', models.FloatField(default=0.0)),
                ('velocidad_ataque', models.CharField(choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('estadistica_principal', 'Estadística Principal'), ('estadistica_adicional', 'Estadística Adicional'), ('recurso', 'Recurso'), ('evento', 'Evento')], max_length=50)),
                ('nivel', models.IntegerField()),
                ('rareza', models.CharField(choices=[('cobre', 'Cobre'), ('hierro', 'Hierro'), ('plata', 'Plata'), ('oro', 'Oro'), ('platino', 'Platino'), ('mithril', 'Mithril'), ('orichalcum', 'Orichalcum'), ('adamantita', 'Adamantita')], max_length=50)),
                ('efecto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progreso', models.TextField()),
                ('fecha_guardado', models.DateTimeField(auto_now_add=True)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jugador')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jugador')),
                ('tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tarjeta')),
            ],
            options={
                'unique_together': {('jugador', 'tarjeta')},
            },
        ),
    ]
