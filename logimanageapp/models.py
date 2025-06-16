from django.db import models

class Requisicao(models.Model):
    # Dados gerais
    fragil = models.BooleanField(default=False)
    liquido = models.BooleanField(default=False)
    toxico = models.BooleanField(default=False)
    refrigerado = models.BooleanField(default=False)
    outro = models.CharField(max_length=255, blank=True)
    embalada = models.BooleanField()
    necessita_embalagem = models.BooleanField()
    tipo_embalagem = models.CharField(max_length=255, blank=True)
    urgente = models.BooleanField()
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
    motivo = models.CharField(max_length=255, blank=True)
    cod_sap = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    comprimento = models.FloatField()
    largura = models.FloatField()
    altura = models.FloatField()
    peso = models.FloatField()
    valor = models.FloatField()
    part_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)

    class Meta:
        db_table = 'logimanageapp_requisicao'

    def __str__(self):
        return f"Requisição #{self.id} - {self.local_origem} para {self.local_coleta}"
