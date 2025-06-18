from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register(r'requisicoes', views.RequisicaoViewSet, basename='requisicao')

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logar_usuario/', views.logar_usuario, name='logar_usuario'),
    path('registro/', views.registro_view, name='registro'),
    path("registrar_usuario/", views.registrar_usuario, name="registrar_usuario"),
    path("home/", views.home_view, name="home"),
    path("requisicao/", views.requisicao_view, name="requisicao"),
    path("perfil/", views.perfil_view, name="perfil"),
    path("formularios/", views.formularios_view, name="formularios"),
    path("painel/", views.painel_view, name="painel"),
    path("teste_view/", views.view_teste, name="teste_view"),
    path("teste_process_requisition_submission/", views.teste_process_requisition_submission, name="teste_processar_requisicao"),
    path("teste_sucesso/", views.teste_sucesso, name="teste_sucesso"),
    path("buscar_equipamento/", views.buscar_equipamento, name="buscar_equipamento"),
    path("processar_requisicao/", views.process_requisition_submission, name="processar_requisicao"),
    path('api/', include(router.urls)),
    path('gerar-requisicao-word/', views.gerar_documento_requisicao, name='gerar_requisicao_word'),
]
