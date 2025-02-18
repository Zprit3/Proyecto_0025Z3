from rest_framework import generics, permissions
from .models import Jugador, Tarjeta, Inventario, Partida
from django.contrib.auth.models import User
from .serializers import JugadorSerializer, TarjetaSerializer, InventarioSerializer, PartidaSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token 
from rest_framework.response import Response



class UserList(generics.ListAPIView):  # Solo para listar usuarios
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Solo el administrador puede ver la lista

class UserDetail(generics.RetrieveAPIView):  # Para ver detalles de un usuario específico
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden ver sus detalles

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        print(f"Datos recibidos: {self.request.data}")  # Imprime los datos recibidos
        user = serializer.save()
        user.set_password(self.request.data['password']) # Usa request.data
        user.save()

class JugadorList(generics.ListCreateAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    permission_classes = [permissions.AllowAny]

class JugadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    permission_classes = [permissions.AllowAny]

class TarjetaList(generics.ListCreateAPIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
    permission_classes = [permissions.AllowAny]

class TarjetaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
    permission_classes = [permissions.AllowAny]

class InventarioList(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [permissions.AllowAny]

class InventarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [permissions.AllowAny]

class PartidaList(generics.ListCreateAPIView):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
    permission_classes = [permissions.AllowAny]

class PartidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
    permission_classes = [permissions.AllowAny]
    

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, _ = Token.objects.get_or_create(user=user)  # Utiliza Token.objects
        return Response({'token': token.key})