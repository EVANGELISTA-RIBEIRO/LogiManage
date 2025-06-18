from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Requisicao(models.Model):
    # Dados gerais
    fragil = models.BooleanField(default=False)
    liquido = models.BooleanField(default=False)
    toxico = models.BooleanField(default=False)
    refrigerado = models.BooleanField(default=False)
    outro = models.CharField(max_length=255, blank=True)
    embalada = models.BooleanField(default=False)
    necessita_embalagem = models.BooleanField(default=False)
    tipo_embalagem = models.CharField(max_length=255, blank=True)
    urgente = models.BooleanField(default=False)
    prazo_maximo = models.DateTimeField()

    # Dados de origem
    local_origem = models.CharField(max_length=255)
    endereco_origem = models.CharField(max_length=255)
    referencia_origem = models.CharField(max_length=255, blank=True)
    responsavel_origem = models.CharField(max_length=100, blank=True, null=True)
    telefone_origem = models.CharField(max_length=20)
    data_origem = models.DateField()
    hora_origem = models.TimeField()
    observacao_origem = models.TextField(blank=True)

    # Dados de destino
    local_destino = models.CharField(max_length=255)
    endereco_destino = models.CharField(max_length=255)
    referencia_destino = models.CharField(max_length=255, blank=True)
    responsavel_destino = models.CharField(max_length=100, blank=True, null=True)
    telefone_destino = models.CharField(max_length=20)
    data_destino = models.DateField()
    hora_destino = models.TimeField()
    observacao_destino = models.TextField(blank=True)

    # Dados do equipamento
    numero_transporte = models.CharField(max_length=50)
    codigo = models.CharField(max_length=100)
    equipamento = models.CharField(max_length=100)
    comprimento = models.FloatField()
    largura = models.FloatField()
    altura = models.FloatField()
    peso = models.FloatField()
    valor = models.FloatField()

    class Meta:
        db_table = 'logimanageapp_requisicao'

    def __str__(self):
        return f"Requisição #{self.id} - {self.local_origem} para {self.local_coleta}"


class Equipamentos(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    valor = models.FloatField()

    class Meta:
        db_table = 'logimanageapp_equipamentos'

    def __str__(self):
        return self.nome
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()