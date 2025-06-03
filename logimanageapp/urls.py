from django.urls import include, path
from rest_framework.routers import DefaultRouter
from logimanageapp.views import (
    home_view,
    login_view,
    registrar_usuario,
    registro_view,
    logar_usuario,
    requisicao_view,
    perfil_view,
    formularios_view,
    painel_view,
    RequisicaoViewSet
)

router = DefaultRouter()
router.register(r'requisicoes', RequisicaoViewSet, basename='requisicao')

urlpatterns = [
    path('', login_view, name='login'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('registro/', registro_view, name='registro'),
    path("registrar_usuario/", registrar_usuario, name="registrar_usuario"),
    path("home/", home_view, name="home"),
    path("requisicao/", requisicao_view, name="requisicao"),
    path("perfil/", perfil_view, name="perfil"),
    path("formularios/", formularios_view, name="formularios"),
    path("painel/", painel_view, name="painel"),
    path('api/', include(router.urls)),
]
