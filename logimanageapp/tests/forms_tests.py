import pytest
from django.contrib.auth.models import User
from logimanageapp.forms import RegistroForm, LoginForm
from django import forms

@pytest.mark.django_db
class TestRegistroForm:
    def test_valid_form(self):
        form = RegistroForm(data={
            'username': 'usuario_teste',
            'email': 'teste@example.com',
            'senha': 'senhaforte123',
            'confirmar_senha': 'senhaforte123'
        })
        assert form.is_valid()

    def test_required_fields(self):
        form = RegistroForm(data={})
        assert not form.is_valid()
        assert 'username' in form.errors
        assert 'email' in form.errors
        assert 'senha' in form.errors
        assert 'confirmar_senha' in form.errors

    def test_password_mismatch(self):
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
        User.objects.create(username="outro_usuario", email="teste@example.com")
        form = RegistroForm(data={
            'username': 'usuario_novo',
            'email': 'teste@example.com',
            'senha': 'senhaforte123',
            'confirmar_senha': 'senhaforte123'
        })
        assert not form.is_valid()
        assert 'email' in form.errors
        assert form.errors['email'][0] == 'Este endereço de e-mail já está em uso!'

    def test_username_cleaning(self):
        form = RegistroForm(data={
            'username': '  usuario com espaco  ',
            'email': 'teste@example.com',
            'senha': 'senhaforte123',
            'confirmar_senha': 'senhaforte123'
        })
        form.is_valid()
        assert form.cleaned_data['username'] == 'usuario_com_espaco'

    def test_password_min_length(self):
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
        form = LoginForm(data={
            'username': 'usuario_teste',
            'password': 'senhaforte123'
        })
        assert form.is_valid()

    def test_required_fields(self):
        form = LoginForm(data={})
        assert not form.is_valid()
        assert 'username' in form.errors
        assert 'password' in form.errors

    def test_widgets(self):
        form = LoginForm()
        assert isinstance(form.fields['username'].widget, forms.TextInput)
        assert isinstance(form.fields['password'].widget, forms.PasswordInput)
