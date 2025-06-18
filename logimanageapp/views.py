from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from docx import Document
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from logimanage import settings
from logimanageapp.models import Profile, Requisicao, Equipamentos
from logimanageapp.serializers import RequisicaoSerializer
from rest_framework.permissions import AllowAny
from logimanageapp.forms import (
    LoginForm,
    ProfileUpdateForm,
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

    requisicoes = Requisicao.objects.all().order_by('-id') # Ordena para garantir ordem consistente

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'active_page': 'requisicao',  # Define a página ativa
        'requisicoes': requisicoes # Passando o objeto de paginação
    }
    return render(request, 'logimanageapp/views/requisicao.html', context)

def buscar_equipamento(request):
    codigo_equipamento = request.GET.get('codigo', None)
    data = {}
    if codigo_equipamento:
        try:
            equipamento = Equipamentos.objects.get(codigo=codigo_equipamento)
            data = {
                'nome': equipamento.nome,
                'valor': str(equipamento.valor) # Converter para string para JSON
            }
        except Equipamentos.DoesNotExist:
            data = {'error': 'Equipamento não encontrado'}
    return JsonResponse(data)

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
            requisicao.codigo = form4.cleaned_data.get('codigo')
            requisicao.equipamento = form4.cleaned_data.get('equipamento')
            requisicao.comprimento = form4.cleaned_data.get('comprimento')
            requisicao.largura = form4.cleaned_data.get('largura')
            requisicao.altura = form4.cleaned_data.get('altura')
            requisicao.peso = form4.cleaned_data.get('peso')
            requisicao.valor = form4.cleaned_data.get('valor')
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

@login_required
def perfil_view(request):
    if request.user.is_authenticated:
        # Tenta obter o perfil do usuário, ou cria um se não existir
        # Isso já é cuidado pelos signals, mas é bom ter o `get_or_create` para robustez
        profile, created = Profile.objects.get_or_create(user=request.user)

        if request.method == 'POST':
            # Se a requisição for POST, processa o formulário de atualização do perfil
            form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                # Adicione uma mensagem de sucesso (opcional, requer django.contrib.messages)
                # messages.success(request, 'Sua foto de perfil foi atualizada com sucesso!')
                return redirect('perfil') # Redireciona para evitar reenvio do formulário
            else:
                # Se o formulário não for válido, os erros estarão em form.errors
                pass # Você pode adicionar lógica para exibir os erros no template
        else:
            # Se a requisição for GET, cria um formulário vazio (ou preenchido com a instância atual)
            form = ProfileUpdateForm(instance=profile)

        context = {
            'user': request.user,
            'profile': profile, # Passa o objeto Profile para o template
            'form': form, # Passa o formulário para o template
            'active_page': 'perfil'  # Define a página ativa
        }
        return render(request, "logimanageapp/views/perfil.html", context)
    else:
        return redirect('login')

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

# Nova View para gerar o documento Word
def gerar_documento_requisicao(request):
    if request.method == 'GET':
        requisicao_id = request.GET.get('numero_transporte')
        
        if not requisicao_id:
            return HttpResponse("Número do Transporte não fornecido.", status=400)

        try:
            requisicao = get_object_or_404(Requisicao, id=requisicao_id)
        except ValueError:
            return HttpResponse("ID de Requisição inválido.", status=400)

        template_path = settings.BASE_DIR / 'doc_templates' / 'Requisicao - LogiManage.docx'
        
        try:
            document = Document(template_path)
        except Exception as e:
            return HttpResponse(f"Erro ao carregar o template do documento: {e}", status=500)

        # --- INÍCIO DA CORREÇÃO ---
        valor_formatado = ''
        try:
            # Tenta converter para float e formatar
            valor_formatado = f"{float(requisicao.valor):.2f}"
        except (ValueError, TypeError):
            # Se não conseguir converter ou for None, define um valor padrão
            valor_formatado = '0.00' 
            # Opcional: Você pode logar este erro para investigar dados inválidos no futuro.
            # import logging
            # logger = logging.getLogger(__name__)
            # logger.warning(f"Campo 'valor' da requisição {requisicao.id} não é um número válido: {requisicao.valor}")
        # --- FIM DA CORREÇÃO ---

        # Dicionário de dados para preencher o documento
        data = {
            'X0': requisicao.equipamento,
            'X1': str(requisicao.comprimento) if requisicao.comprimento is not None else '',
            'X2': str(requisicao.largura) if requisicao.largura is not None else '',
            'X3': str(requisicao.altura) if requisicao.altura is not None else '',
            'X4': str(requisicao.peso) if requisicao.peso is not None else '',
            'X5': valor_formatado, # <--- Linha CORRIGIDA

            # Booleanos com (X) ou ()
            'X6': '(X)' if requisicao.fragil else '()',
            'X7': '(X)' if requisicao.liquido else '()',
            'X8': '(X)' if requisicao.toxico else '()',
            'X9': '(X)' if requisicao.refrigerado else '()',

            'Y1': requisicao.outro if requisicao.outro else 'Nenhum',

            # Booleanos com Sim/Não
            'Y2': 'Sim' if requisicao.embalada else 'Não',
            'Y3': 'Sim' if requisicao.necessita_embalagem else 'Não',
            
            'Y4': requisicao.tipo_embalagem if requisicao.tipo_embalagem else '',
            'Y5': 'Sim' if requisicao.urgente else 'Não',
            'Y6': requisicao.prazo_maximo.strftime('%d/%m/%Y %H:%M') if requisicao.prazo_maximo else '',

            'Y7': requisicao.local_origem,
            'Y8': requisicao.data_origem.strftime('%d/%m/%Y') if requisicao.data_origem else '',
            'Y9': requisicao.hora_origem.strftime('%H:%M') if requisicao.hora_origem else '',
            'Z1': requisicao.endereco_origem,
            'Z2': requisicao.referencia_origem if requisicao.referencia_origem else '',
            'Z3': requisicao.observacao_origem if requisicao.observacao_origem else 'Nenhuma',
            'Z4': requisicao.responsavel_origem if requisicao.responsavel_origem else '',
            'Z5': requisicao.telefone_origem,

            'Z6': requisicao.local_destino,
            'Z7': requisicao.data_destino.strftime('%d/%m/%Y') if requisicao.data_destino else '',
            'Z8': requisicao.hora_destino.strftime('%H:%M') if requisicao.hora_destino else '',
            'Z9': requisicao.endereco_destino,
            'W1': requisicao.referencia_destino if requisicao.referencia_destino else '',
            'W2': requisicao.observacao_destino if requisicao.observacao_destino else 'Nenhuma',
            'W3': requisicao.responsavel_destino if requisicao.responsavel_destino else '',
            'W4': requisicao.telefone_destino,

            'W5': str(requisicao.id)
        }

        # ... (restante da sua função para substituir texto nos parágrafos e tabelas) ...
        for paragraph in document.paragraphs:
            for key, value in data.items():
                if key in ['X6', 'X7', 'X8', 'X9']:
                    if ' ' + key + ' ' in paragraph.text:
                        replacement = value.strip('()')
                        paragraph.text = paragraph.text.replace(' ' + key + ' ', f' {replacement} ')
                    # Adicionalmente, caso não tenha espaços ao redor (menos provável, mas para robustez)
                    elif key in paragraph.text:
                        replacement = value.strip('()')
                        paragraph.text = paragraph.text.replace(key, replacement)
                else:
                    if key in paragraph.text:
                        paragraph.text = paragraph.text.replace(key, str(value))
        
        for table in document.tables:
            for row in table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        for key, value in data.items():
                            if key in ['X6', 'X7', 'X8', 'X9']:
                                if ' ' + key + ' ' in paragraph.text:
                                    replacement = value.strip('()')
                                    paragraph.text = paragraph.text.replace(' ' + key + ' ', f' {replacement} ')
                                elif key in paragraph.text:
                                    replacement = value.strip('()')
                                    paragraph.text = paragraph.text.replace(key, replacement)
                            else:
                                if key in paragraph.text:
                                    paragraph.text = paragraph.text.replace(key, str(value))


        # Salva o documento em um buffer de memória
        buffer = BytesIO()
        document.save(buffer)
        buffer.seek(0)

        file_name = f"Requisicao_{requisicao_id}.docx"
        response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    
    return HttpResponse("Método não permitido.", status=405)