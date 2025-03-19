from django.urls import path
from logimanageapp.views import *

urlpatterns = [
    path('login/', login_view, name='login'), # Página de login
    path('', registro_view, name='registro'), # Página registro
    path("registrar_usuario/", registrar_usuario, name="registrar_usuario"), # Registra o usuário
]
