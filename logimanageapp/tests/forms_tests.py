import pytest
from django.contrib.auth.models import User
from logimanageapp.forms import RegistroForm, LoginForm
from django import forms

@pytest.mark.django_db
class TestRegistroForm:
    def test_valid_form(self):
        # CT-001: Validação de um formulário de registro com dados válidos.
        # Esperado: O formulário deve ser válido.
        form = RegistroForm(data={
            'username': 'usuario_teste',
            'email': 'teste@example.com',
            'senha': 'senhaforte123',
            'confirmar_senha': 'senhaforte123'
        })
        assert form.is_valid()

    def test_required_fields(self):
        # CT-002: Validação de campos obrigatórios no formulário de registro.
        # Esperado: O formulário deve ser inválido e exibir mensagens de erro para os campos ausentes.
        form = RegistroForm(data={})
        assert not form.is_valid()
        assert 'username' in form.errors
        assert 'email' in form.errors
        assert 'senha' in form.errors
        assert 'confirmar_senha' in form.errors

    def test_password_mismatch(self):
        # CT-003: Validação de senhas diferentes no formulário de registro.
        # Esperado: O formulário deve ser inválido e exibir mensagem de senhas não coincidem.
        form = RegistroForm(data={
            'username': 'usuario_teste',
            'email': 'teste@example.com',
            'senha': 'senhaforte123',
            'confirmar_senha': 'outrasenha123'
        })
        assert not form.is_valid()
        assert 'confirmar_senha' in form.errors
        assert form.errors['confirmar_senha'][0] == 'As senhas não coincidem!'

    def test_email_already_exists(self, db):
        # CT-004: Validação de e-mail já cadastrado no formulário de registro.
        # Esperado: O formulário deve ser inválido e exibir mensagem de e-mail já em uso.
        User.objects.create(username="outro_usuario", email="teste@example.com")
        form = RegistroForm(data={
            'username': 'usuario_novo',
            'email': 'teste@example.com',
            'senha': 'senhaforte123',
            'confirmar_senha': 'senhaforte123'
        })
        assert not form.is_valid()
        assert 'email' in form.errors
        # Observação: Mensagem esperada no plano de testes é 'Este endereço de e-mail já está em uso!'
        assert form.errors['email'][0] == 'Este endereço de e-mail já está em uso!'

    def test_username_cleaning(self):
        # CT-005: Validação da limpeza do nome de usuário no formulário de registro.
        # Esperado: O nome de usuário deve ser salvo sem espaços extras.
        form = RegistroForm(data={
            'username': '  usuario com espaco  ',
            'email': 'teste@example.com',
            'senha': 'senhaforte123',
            'confirmar_senha': 'senhaforte123'
        })
        form.is_valid()
        assert form.cleaned_data['username'] == 'usuario_com_espaco'

    def test_password_min_length(self):
        # CT-006: Validação de senha curta no formulário de registro.
        # Esperado: O formulário deve ser inválido e exibir mensagem sobre tamanho mínimo da senha.
        form = RegistroForm(data={
            'username': 'usuario_teste',
            'email': 'teste@example.com',
            'senha': '123',
            'confirmar_senha': '123'
        })
        assert not form.is_valid()
        assert 'senha' in form.errors
        assert 'Sua senha deve ter no mínimo 8 caracteres!' in form.errors['senha']


@pytest.mark.django_db
class TestLoginForm:
    def test_valid_login_form(self):
        # CT-007: Validação de um formulário de login com dados válidos.
        # Esperado: O formulário deve ser válido.
        form = LoginForm(data={
            'username': 'usuario_teste',
            'password': 'senhaforte123'
        })
        assert form.is_valid()

    def test_required_fields(self):
        # CT-008: Validação de campos obrigatórios no formulário de login.
        # Esperado: O formulário deve ser inválido e exibir mensagens de erro para os campos ausentes.
        form = LoginForm(data={})
        assert not form.is_valid()
        assert 'username' in form.errors
        assert 'password' in form.errors

    def test_widgets(self):
        # CT-009: Validação dos widgets dos campos no formulário de login.
        # Esperado: username deve ser TextInput e password deve ser PasswordInput.
        form = LoginForm()
        assert isinstance(form.fields['username'].widget, forms.TextInput)
        assert isinstance(form.fields['password'].widget, forms.PasswordInput)
