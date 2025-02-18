"""
Explicación del código

    Importamos las clases necesarias de rest_framework.serializers y los modelos que definimos en models.py.
    Creamos una clase serializer para cada modelo (JugadorSerializer, TarjetaSerializer, etc.).
    Dentro de cada clase serializer, definimos una clase Meta que especifica el modelo al que está asociado el serializer y 
    los campos que se incluirán en la serialización. En este caso, hemos utilizado fields = '__all__' para incluir todos los campos de cada modelo.
"""

from rest_framework import serializers
from .models import Jugador, Tarjeta, Inventario, Partida
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Campo para la contraseña

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')  # Incluye la contraseña
        extra_kwargs = {'username': {'required': True}} # Asegura que el username sea requerido

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = "__all__"


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = "__all__"


class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = "__all__"


