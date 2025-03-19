from django  import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    senha = forms.CharField(
            widget = forms.PasswordInput(attrs={'class': 'input-field'}),
            min_length = 8,
            label ='Senha'
    )
    confirmar_senha = forms.CharField(
        widget = forms.PasswordInput(attrs={'class': 'input-field'}),
        label ='Confirme sua Senha'
    )
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={'class': 'input-field'}),
        label = 'E-mail',
        required = True,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'senha']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field'}),
            'email': forms.EmailInput(attrs={'class': 'input-field'}),
        }
        labels = {
            'username': 'Nome de Usuário',
            'email': 'E-mail',
        }
        help_texts = {
            'username': '',
        }
        error_messages = {
            'username': {
                'required': 'Por favor informe um nome de usuário!',
                'unique': 'Este nome de usuário já está em uso!',
                'max_length': 'O nome de usuário deve conter apenas letras, números e os caracteres @/./+/-/_ e deve ter no mínimo 5 caracteres!',
                'invalid': 'O nome de usuário deve conter apenas letras, números e os caracteres @/./+/-/_ e deve ter no mínimo 5 caracteres!',
            },
            'email': {
                'required': 'Por favor informe um endereço de e-mail!',
                'unique': 'Este endereço de e-mail já está em uso!',
                'invalid': 'Por favor informe um endereço de e-mail válido!',
            },
            'senha': {
                'required': 'Por favor informe uma senha!',
                'min_length': 'Sua senha deve ter no mínimo 8 caracteres!',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', 'As senhas não coincidem!')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.strip().replace(' ', '_')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este endereço de e-mail já está em uso!')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'input-field'}),
        label='Nome de Usuário'
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'class': 'input-field'}),
        label='Senha'
    )