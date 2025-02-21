from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('jugadores/', views.JugadorList.as_view(), name='jugador-list'),
    path('jugadores/<int:pk>/', views.JugadorDetail.as_view(), name='jugador-detail'),
    path('tarjetas/', views.TarjetaList.as_view(), name='tarjeta-list'),
    path('tarjetas/<int:pk>/', views.TarjetaDetail.as_view(), name='tarjeta-detail'),
    path('inventarios/', views.InventarioList.as_view(), name='inventario-list'),
    path('inventarios/<int:pk>/', views.InventarioDetail.as_view(), name='inventario-detail'),
    path('partidas/', views.PartidaList.as_view(), name='partida-list'),
    path('partidas/<int:pk>/', views.PartidaDetail.as_view(), name='partida-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('users/create/', views.UserCreate.as_view(), name='user-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]