from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from logimanageapp.models import Requisicao
from logimanageapp.serializers import RequisicaoSerializer
from rest_framework.permissions import AllowAny
from logimanageapp.forms import (
    LoginForm,
    RegistroForm,
    RequisicaoFormEtapa1,
    RequisicaoFormEtapa2,
    RequisicaoFormEtapa3,
    RequisicaoFormEtapa4,
)

def registro_view(request):
    form = RegistroForm(
        initial={
            "username": "",
            "email": "",
            "senha": "",
            "confirmar_senha": ""
        })
    return render(request, "logimanageapp/views/registro.html", {"form": form})

def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["senha"])
            user.save()
            login(request, user)
            return redirect("login")
    else:
        form = RegistroForm()

    return render(request, "logimanageapp/views/registro.html", {"form": form})

def login_view(request):
    form = LoginForm(
        initial={
            "email": "",
            "password": ""
        })
    return render(request, "logimanageapp/views/login.html", {"form": form})

def logar_usuario(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Usuário ou senha inválidos")

    else:
        form = LoginForm()

    return render(request, "logimanageapp/views/login.html", {"form": form})

def home_view(request):
    context = {
        'active_page': 'home'  # Define a página ativa
    }
    return render(request, "logimanageapp/views/home.html", context)

def requisicao_view(request):
    form1 = RequisicaoFormEtapa1()
    form2 = RequisicaoFormEtapa2()
    form3 = RequisicaoFormEtapa3()
    form4 = RequisicaoFormEtapa4()

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'active_page': 'requisicao'  # Define a página ativa
    }
    return render(request, 'logimanageapp/views/requisicao.html', context)

def process_requisition_submission(request):
    if request.method == 'POST':
        form1 = RequisicaoFormEtapa1(request.POST)
        form2 = RequisicaoFormEtapa2(request.POST)
        form3 = RequisicaoFormEtapa3(request.POST)
        form4 = RequisicaoFormEtapa4(request.POST)

        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            # Crie uma instância vazia
            requisicao = Requisicao()

            # Atribuir dados do form1
            requisicao.fragil = form1.cleaned_data.get('fragil')
            requisicao.liquido = form1.cleaned_data.get('liquido')
            requisicao.refrigerado = form1.cleaned_data.get('refrigerado')
            requisicao.toxico = form1.cleaned_data.get('toxico')
            requisicao.outro = form1.cleaned_data.get('outro')
            requisicao.embalada = form1.cleaned_data.get('embalada')
            requisicao.necessita_embalagem = form1.cleaned_data.get('necessita_embalagem')
            requisicao.tipo_embalagem = form1.cleaned_data.get('tipo_embalagem')
            requisicao.urgente = form1.cleaned_data.get('urgente')
            requisicao.prazo_maximo = form1.cleaned_data.get('prazo_maximo')

            # Atribuir dados do form2
            requisicao.local_origem = form2.cleaned_data.get('local_origem')
            requisicao.endereco_origem = form2.cleaned_data.get('endereco_origem')
            requisicao.referencia_origem = form2.cleaned_data.get('referencia_origem')
            requisicao.responsavel_origem = form2.cleaned_data.get('responsavel_origem')
            requisicao.telefone_origem = form2.cleaned_data.get('telefone_origem')
            requisicao.data_origem = form2.cleaned_data.get('data_origem')
            requisicao.hora_origem = form2.cleaned_data.get('hora_origem')
            requisicao.observacao_origem = form2.cleaned_data.get('observacao_origem')

            # Atribuir dados do form3
            requisicao.local_destino = form3.cleaned_data.get('local_destino')
            requisicao.endereco_destino = form3.cleaned_data.get('endereco_destino')
            requisicao.referencia_destino = form3.cleaned_data.get('referencia_destino')
            requisicao.responsavel_destino = form3.cleaned_data.get('responsavel_destino')
            requisicao.telefone_destino = form3.cleaned_data.get('telefone_destino')
            requisicao.data_destino = form3.cleaned_data.get('data_destino')
            requisicao.hora_destino = form3.cleaned_data.get('hora_destino')
            requisicao.observacao_destino = form3.cleaned_data.get('observacao_destino')

            # Atribuir dados do form4
            requisicao.numero_transporte = form4.cleaned_data.get('numero_transporte')
            requisicao.motivo = form4.cleaned_data.get('motivo')
            requisicao.cod_sap = form4.cleaned_data.get('cod_sap')
            requisicao.alias = form4.cleaned_data.get('alias')
            requisicao.comprimento = form4.cleaned_data.get('comprimento')
            requisicao.largura = form4.cleaned_data.get('largura')
            requisicao.altura = form4.cleaned_data.get('altura')
            requisicao.peso = form4.cleaned_data.get('peso')
            requisicao.valor = form4.cleaned_data.get('valor')
            requisicao.serial_number = form4.cleaned_data.get('serial_number')
            requisicao.part_number = form4.cleaned_data.get('part_number')
            requisicao.save()
            return redirect('requisicao')  # Redireciona para a página de requisição após salvar
        else:
            # Se a validação falhar, re-renderiza a página de requisição com os formulários e seus erros
            # Isso mostrará ao usuário quais campos precisam de correção.
            context = {
                'form1': form1,
                'form2': form2,
                'form3': form3,
                'form4': form4,
                'active_page': 'requisicao'
            }
            return render(request, 'logimanageapp/views/requisicao.html', context)
    else:
        # Se não for uma requisição POST, redirecionar ou renderizar um conjunto de formulários vazio
        return redirect('requisicao') # Ou renderizar com formulários vazios como feito em requisicao_view

def perfil_view(request):
    context = {
        'active_page': 'perfil'  # Define a página ativa
    }
    return render(request, "logimanageapp/views/perfil.html", context)

def formularios_view(request):
    context = {
        'active_page': 'formularios'  # Define a página ativa
    }
    return render(request, "logimanageapp/views/formularios.html", context)

def painel_view(request):
    context = {
        'active_page': 'painel'  # Define a página ativa
    }
    return render(request, "logimanageapp/views/painel.html", context)

class RequisicaoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar as requisições de transporte.
    Permite listar, criar, atualizar e deletar requisições.
    """

    permission_classes = [AllowAny]
    queryset = Requisicao.objects.all()
    serializer_class = RequisicaoSerializer

def view_teste(request):
    form1 = RequisicaoFormEtapa1()
    form2 = RequisicaoFormEtapa2()
    form3 = RequisicaoFormEtapa3()
    form4 = RequisicaoFormEtapa4()
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
    }
    return render(request, "logimanageapp/views/teste_form.html", context)

def teste_process_requisition_submission(request):
    if request.method == 'POST':
        # Aqui você precisaria de uma lógica para lidar com cada etapa
        # Por simplicidade, vou demonstrar como você poderia criar uma instância de Requisicao
        # e preencher os campos. Em um cenário real, você provavelmente usaria
        # sessions para guardar os dados de cada etapa ou enviar tudo de uma vez.

        # Exemplo simplificado para pegar os dados e salvar (idealmente, validaria cada etapa)
        form1 = RequisicaoFormEtapa1(request.POST)
        form2 = RequisicaoFormEtapa2(request.POST)
        form3 = RequisicaoFormEtapa3(request.POST)
        form4 = RequisicaoFormEtapa4(request.POST)

        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            # Crie uma instância vazia
            requisicao = Requisicao()

            # Preencha com os dados de cada formulário
            for field in form1.cleaned_data:
                setattr(requisicao, field, form1.cleaned_data[field])
            for field in form2.cleaned_data:
                setattr(requisicao, field, form2.cleaned_data[field])
            for field in form3.cleaned_data:
                setattr(requisicao, field, form3.cleaned_data[field])
            for field in form4.cleaned_data:
                setattr(requisicao, field, form4.cleaned_data[field])

            requisicao.save()
            return redirect('teste_sucesso') # Redirecione para uma página de sucesso
        else:
            # Se a validação falhar, você precisaria decidir como mostrar os erros
            # e qual modal reabrir. Para este exemplo, apenas re-renderizaremos.
            # Em um cenário real, você pode precisar de mais lógica aqui.
            pass # A lógica de re-renderização está no template JS/HTML
    else:
        form1 = RequisicaoFormEtapa1()
        form2 = RequisicaoFormEtapa2()
        form3 = RequisicaoFormEtapa3()
        form4 = RequisicaoFormEtapa4()

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
    }
    return render(request, 'logimanageapp/views/requisicao.html', context)

def teste_sucesso(request):
    return render(request, 'logimanageapp/views/teste_sucesso.html') # Crie um template simples de sucesso
