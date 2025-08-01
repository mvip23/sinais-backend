from rest_framework import serializers
from .models import TransferenciaEstoque

class TransferenciaEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferenciaEstoque
        fields = '__all__' 