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
    RequisicaoViewSet,
    teste_process_requisition_submission, # Teste function
    teste_sucesso, # Teste function
    view_teste, # Teste function
    process_requisition_submission
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
    path("teste_view/", view_teste, name="teste_view"),
    path("teste_process_requisition_submission/", teste_process_requisition_submission, name="teste_processar_requisicao"),
    path("teste_sucesso/", teste_sucesso, name="teste_sucesso"),
    path("processar_requisicao/", process_requisition_submission, name="processar_requisicao"),
    path('api/', include(router.urls)),
]
