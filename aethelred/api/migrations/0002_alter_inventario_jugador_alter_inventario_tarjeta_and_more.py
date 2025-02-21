# Generated by Django 5.1.6 on 2025-02-21 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='jugador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventarios', to='api.jugador'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='tarjeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventarios', to='api.tarjeta'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='nombre',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='partida',
            name='jugador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidas', to='api.jugador'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='progreso',
            field=models.JSONField(),
        ),
    ]
