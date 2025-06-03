from rest_framework import serializers
from logimanageapp.models import Requisicao

class RequisicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisicao
        fields = '__all__'