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

# Definição de choices (se já não estiver em models.py ou outro lugar)
SIM_NAO_CHOICES = [
    ('sim', 'Sim'),
    ('nao', 'Não'),
]

class RequisicaoFormEtapa1(forms.ModelForm):
    # Definindo campos personalizados para adicionar widgets com 'input-text'
    # Os campos que já estão no Meta.widgets ou são RadioSelect/CheckboxInput
    # não precisam ser redefinidos aqui, a menos que queira adicionar attrs extras.
    # Vou adicionar 'input-text' nos campos textuais via Meta.widgets diretamente.

    class Meta:
        model = Requisicao
        fields = [
            'fragil', 'liquido', 'toxico', 'refrigerado', 'outro', 'prazo_maximo',
            'embalada', 'necessita_embalagem', 'tipo_embalagem', 'urgente',
        ]
        widgets = {
            'prazo_maximo': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'input-text'}),
            'fragil': forms.CheckboxInput(attrs={'class': 'checkbox-input'}), # Se o CSS modal.css usar uma classe para checkboxes
            'liquido': forms.CheckboxInput(attrs={'class': 'checkbox-input'}),
            'toxico': forms.CheckboxInput(attrs={'class': 'checkbox-input'}),
            'refrigerado': forms.CheckboxInput(attrs={'class': 'checkbox-input'}),
            'embalada': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'necessita_embalagem': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'urgente': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            # Adicionando 'input-text' para campos de texto
            'outro': forms.TextInput(attrs={'class': 'input-text'}),
            'tipo_embalagem': forms.TextInput(attrs={'class': 'input-text'}),
        }
        labels = {
            'fragil': 'Frágil',
            'liquido': 'Líquido',
            'toxico': 'Tóxico',
            'refrigerado': 'Refrigerado',
            'outro': 'Outros',
            'embalada': 'A carga a ser transportada já está embalada?',
            'necessita_embalagem': 'Será necessário algum tipo de embalagem?',
            'tipo_embalagem': 'Tipo de Embalagem',
            'urgente': 'Urgente?',
            'prazo_maximo': 'Qual o prazo máximo?',
        }

class RequisicaoFormEtapa2(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = [
            'local_origem', 'endereco_origem', 'referencia_origem', 'responsavel_origem',
            'telefone_origem', 'data_origem', 'hora_origem', 'observacao_origem'
        ]
        widgets = {
            'local_origem': forms.TextInput(attrs={'class': 'input-text'}),
            'endereco_origem': forms.TextInput(attrs={'class': 'input-text'}),
            'referencia_origem': forms.TextInput(attrs={'class': 'input-text'}),
            'responsavel_origem': forms.TextInput(attrs={'class': 'input-text'}),
            'telefone_origem': forms.TextInput(attrs={'class': 'input-text'}),
            'data_origem': forms.DateInput(attrs={'type': 'date', 'class': 'input-text'}),
            'hora_origem': forms.TimeInput(attrs={'type': 'time', 'class': 'input-text'}),
            'observacao_origem': forms.Textarea(attrs={'class': 'input-text', 'rows': 3}), # Defini 'rows' para manter a altura
        }
        labels = {
            'local_origem': 'Local Origem',
            'endereco_origem': 'Endereço de Origem',
            'referencia_origem': 'Ponto de Referência',
            'responsavel_origem': 'Responsável pela Carga',
            'telefone_origem': 'Telefone do Responsável',
            'data_origem': 'Data da Coleta',
            'hora_origem': 'Hora da Coleta',
            'observacao_origem': 'Observações',
        }
        error_messages = {
            'local_origem': {'required': 'Por favor informe o local de origem!'},
            'endereco_origem': {'required': 'Por favor informe o endereço de origem!'},
            'telefone_origem': {'required': 'Por favor informe o telefone do responsável pela carga!'},
        }


class RequisicaoFormEtapa3(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = [
            'local_destino', 'endereco_destino', 'referencia_destino', 'responsavel_destino',
            'telefone_destino', 'data_destino', 'hora_destino', 'observacao_destino'
        ]
        widgets = {
            'local_destino': forms.TextInput(attrs={'class': 'input-text'}),
            'endereco_destino': forms.TextInput(attrs={'class': 'input-text'}),
            'referencia_destino': forms.TextInput(attrs={'class': 'input-text'}),
            'responsavel_destino': forms.TextInput(attrs={'class': 'input-text'}),
            'telefone_destino': forms.TextInput(attrs={'class': 'input-text'}),
            'data_destino': forms.DateInput(attrs={'type': 'date', 'class': 'input-text'}),
            'hora_destino': forms.TimeInput(attrs={'type': 'time', 'class': 'input-text'}),
            'observacao_destino': forms.Textarea(attrs={'class': 'input-text', 'rows': 3}), # Defini 'rows' para manter a altura
        }
        labels = {
            'local_destino': 'Local Destino',
            'endereco_destino': 'Endereço de Destino',
            'referencia_destino': 'Ponto de Referência',
            'responsavel_destino': 'Responsável pela Entrega',
            'telefone_destino': 'Telefone do Responsável',
            'data_destino': 'Data da Entrega',
            'hora_destino': 'Hora da Entrega',
            'observacao_destino': 'Observação',
        }
        error_messages = {
            'local_destino': {'required': 'Por favor informe o local de destino!'},
            'endereco_destino': {'required': 'Por favor informe o endereço de destino!'},
            'telefone_destino': {'required': 'Por favor informe o telefone do responsável!'},
        }

class RequisicaoFormEtapa4(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = [
            'numero_transporte', 'motivo', 'cod_sap', 'alias',
            'comprimento', 'largura', 'altura', 'peso', 'valor',
            'part_number', 'serial_number'
        ]
        widgets = {
            'numero_transporte': forms.TextInput(attrs={'class': 'input-text'}),
            'motivo': forms.TextInput(attrs={'class': 'input-text'}),
            'cod_sap': forms.TextInput(attrs={'class': 'input-text'}),
            'alias': forms.TextInput(attrs={'class': 'input-text'}),
            'comprimento': forms.NumberInput(attrs={'class': 'input-text'}), # Assumindo que são campos numéricos
            'largura': forms.NumberInput(attrs={'class': 'input-text'}),
            'altura': forms.NumberInput(attrs={'class': 'input-text'}),
            'peso': forms.NumberInput(attrs={'class': 'input-text'}),
            'valor': forms.NumberInput(attrs={'class': 'input-text'}),
            'part_number': forms.TextInput(attrs={'class': 'input-text'}),
            'serial_number': forms.TextInput(attrs={'class': 'input-text'}),
        }
        labels = {
            'numero_transporte': 'Nº Transporte',
            'motivo': 'Motivo',
            'cod_sap': 'COD (SAP)',
            'alias': 'Alias',
            'comprimento': 'Comprimento (cm)',
            'largura': 'Largura (cm)',
            'altura': 'Altura (cm)',
            'peso': 'Peso (kg)',
            'valor': 'Valor',
            'part_number': 'Part Number',
            'serial_number': 'Serial Number',
        }
