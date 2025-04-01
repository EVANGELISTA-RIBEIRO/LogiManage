from django.urls import path
from logimanageapp.views import (
    home_view,
    login_view,
    registrar_usuario,
    registro_view,
)

urlpatterns = [
    # Página de login
    path('login/', login_view, name='login'),
    # Página registro
    path('', registro_view, name='registro'),
    # Registra o usuário
    path("registrar_usuario/", registrar_usuario, name="registrar_usuario"),
    # Página home
    path("home/", home_view, name="home"),
]
