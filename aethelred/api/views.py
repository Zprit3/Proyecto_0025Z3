from rest_framework import generics, permissions
from .models import Jugador, Tarjeta, Inventario, Partida
from django.contrib.auth.models import User
from .serializers import JugadorSerializer, TarjetaSerializer, InventarioSerializer, PartidaSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data['password'])
        user.save()

class JugadorList(generics.ListCreateAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class JugadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class TarjetaList(generics.ListCreateAPIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated] 

class TarjetaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated] 

class InventarioList(generics.ListCreateAPIView):
    queryset = Inventario.objects.select_related('jugador', 'tarjeta').all()
    serializer_class = InventarioSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated] 

class InventarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.select_related('jugador', 'tarjeta').all()
    serializer_class = InventarioSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated] 

class PartidaList(generics.ListCreateAPIView):
    queryset = Partida.objects.select_related('jugador').all()
    serializer_class = PartidaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class PartidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partida.objects.select_related('jugador').all()
    serializer_class = PartidaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]