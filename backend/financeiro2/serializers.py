from rest_framework import serializers
from .models import Receita, Despesa, AnexoComprovante

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

class AnexoComprovanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnexoComprovante
        fields = '__all__' 