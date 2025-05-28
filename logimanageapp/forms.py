from django  import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

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

class RequisicaoForm(forms.Form):
    # --- Dados sobre o Equipamento ---
    PECULIARIDADES_CHOICES = [
        ('fragil', 'Frágil'),
        ('liquido', 'Líquido'),
        ('refrigerado', 'Refrigerado'),
        ('toxico', 'Tóxico'),
    ]

    peculiaridades = forms.MultipleChoiceField(
        choices=PECULIARIDADES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="A carga possui alguma peculiaridade?",
        required=False
    )

    outra_peculiaridade = forms.CharField(
        label="Outro",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Especifique'})
    )

    embalada = forms.ChoiceField(
        choices=[('sim', 'Sim'), ('nao', 'Não')],
        widget=forms.RadioSelect,
        label="A carga a ser transportada já está embalada?"
    )

    necessita_embalagem = forms.ChoiceField(
        choices=[('sim', 'Sim'), ('nao', 'Não')],
        widget=forms.RadioSelect,
        label="Será necessário algum tipo de embalagem?"
    )

    tipo_embalagem = forms.CharField(
        label="Tipo de Embalagem",
        required=False
    )

    urgente = forms.ChoiceField(
        choices=[('sim', 'Sim'), ('nao', 'Não')],
        widget=forms.RadioSelect,
        label="Urgente?"
    )

    prazo_maximo = forms.CharField(
        label="Qual o prazo máximo?",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'dd/mm/aaaa'})
    )

    # --- Dados de Origem ---
    local_origem = forms.CharField(label="Local Origem")
    endereco_origem = forms.CharField(label="Endereço de Origem")
    referencia_origem = forms.CharField(label="Ponto de Referência", required=False)
    telefone_origem = forms.CharField(label="Telefone do Responsável")
    data_coleta_origem = forms.DateField(label="Data da Coleta", widget=forms.DateInput(attrs={'type': 'date'}))
    hora_coleta_origem = forms.TimeField(label="Hora da Coleta", widget=forms.TimeInput(attrs={'type': 'time'}))
    observacao_origem = forms.CharField(label="Observação", required=False, widget=forms.Textarea)

    # --- Dados da Coleta (iguais aos de origem) ---
    local_coleta = forms.CharField(label="Local Coleta")
    endereco_coleta = forms.CharField(label="Endereço de Coleta")
    referencia_coleta = forms.CharField(label="Ponto de Referência", required=False)
    telefone_coleta = forms.CharField(label="Telefone do Responsável")
    data_coleta = forms.DateField(label="Data da Coleta", widget=forms.DateInput(attrs={'type': 'date'}))
    hora_coleta = forms.TimeField(label="Hora da Coleta", widget=forms.TimeInput(attrs={'type': 'time'}))
    observacao_coleta = forms.CharField(label="Observação", required=False, widget=forms.Textarea)

