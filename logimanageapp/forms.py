from django  import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

from logimanageapp.models import Requisicao

class RegistroForm(forms.ModelForm):
    senha = forms.CharField(
            widget = forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Insira sua senha'}),
            validators=[MinLengthValidator(8, message='Sua senha deve ter no mínimo 8 caracteres!')],
            label ='Senha'
    )
    confirmar_senha = forms.CharField(
        widget = forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Insira a senha novamente'}),
        label ='Confirmar Senha'
    )
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Insira seu e-mail'}),
        label = 'E-mail',
        required = True,
    )
    username = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Insira seu nome'}),
        label = 'Nome',
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'senha']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field'}),
            'email': forms.EmailInput(attrs={'class': 'input-field'}),
        }
        labels = {
            'username': 'Nome',
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
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Insira seu nome'}),
        label="Nome",
        required=True,
        error_messages={
            'required': 'Por favor informe seu nome de usuário!',
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': '••••••••'}),
        label="Senha",
        validators=[MinLengthValidator(8, message='A senha deve ter no mínimo 8 caracteres!')],
        error_messages={
            'required': 'Por favor informe sua senha!',
        }
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.strip().replace(' ', '_')

from django import forms
from .models import Requisicao

class RequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = '__all__'
        widgets = {
            'prazo_maximo': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_coleta_origem': forms.DateInput(attrs={'type': 'date'}),
            'hora_coleta_origem': forms.TimeInput(attrs={'type': 'time'}),
            'data_coleta': forms.DateInput(attrs={'type': 'date'}),
            'hora_coleta': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'peculiaridades': 'A carga possui alguma peculiaridade?',
            'outro': 'Outro',
            'embalada': 'A carga a ser transportada já está embalada?',
            'necessita_embalagem': 'Será necessário algum tipo de embalagem?',
            'tipo_embalagem': 'Tipo de Embalagem',
            'urgente': 'Urgente?',
            'prazo_maximo': 'Qual o prazo máximo?',
            'local_origem': 'Local Origem',
            'endereco_origem': 'Endereço de Origem',
            'referencia_origem': 'Ponto de Referência',
            'telefone_origem': 'Telefone do Responsável',
            'data_coleta_origem': 'Data da Coleta',
            'hora_coleta_origem': 'Hora da Coleta',
            'observacao_origem': 'Observação',
            'local_coleta': 'Local Coleta',
            'endereco_coleta': 'Endereço de Coleta',
            'referencia_coleta': 'Ponto de Referência',
            'telefone_coleta': 'Telefone do Responsável',
            'data_coleta': 'Data da Coleta',
            'hora_coleta': 'Hora da Coleta',
            'observacao_coleta': 'Observação',
            'numero_transporte': 'Nº Transporte',
            'motivo': 'Motivo',
            'cod_sap': 'COD (SAP)',
            'alias': 'Alías',
            'comprimento': 'Comprimento',
            'largura': 'Largura',
            'altura': 'Altura',
            'peso': 'Peso',
            'valor': 'Valor',
            'part_number': 'Part Number',
            'serial_number': 'Serial Number',
        }
        help_texts = {
            'peculiaridades': 'Descreva as peculiaridades da carga, se houver.',
            'outro': 'Especifique outro tipo de embalagem, se necessário.',
            'tipo_embalagem': 'Informe o tipo de embalagem necessária, se aplicável.',
            'observacao_origem': 'Observações adicionais sobre a origem da carga.',
            'observacao_coleta': 'Observações adicionais sobre a coleta da carga.',
        }
        error_messages = {
            'local_origem': {
                'required': 'Por favor informe o local de origem!',
            },
            'endereco_origem': {
                'required': 'Por favor informe o endereço de origem!',
            },
            'telefone_origem': {
                'required': 'Por favor informe o telefone do responsável pela carga!',
            },
            'local_coleta': {
                'required': 'Por favor informe o local de coleta!',
            },
            'endereco_coleta': {
                'required': 'Por favor informe o endereço de coleta!',
            },
            'telefone_coleta': {
                'required': 'Por favor informe o telefone do responsável pela coleta!',
            },
        }