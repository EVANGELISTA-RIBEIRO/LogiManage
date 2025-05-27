from django.urls import path
from logimanageapp.views import (
    home_view,
    login_view,
    registrar_usuario,
    registro_view,
    logar_usuario,
    requisicao_view,
)

urlpatterns = [
    path('', login_view, name='login'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('registro/', registro_view, name='registro'),
    path("registrar_usuario/", registrar_usuario, name="registrar_usuario"),
    path("home/", home_view, name="home"),
    path("requisicao/", requisicao_view, name="requisicao"),
]
