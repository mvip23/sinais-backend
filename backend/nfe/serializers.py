from rest_framework import serializers
from .models import NFe

class NFeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFe
        fields = '__all__' 