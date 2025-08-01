from rest_framework import serializers
from .models import Deposito

class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = '__all__' 