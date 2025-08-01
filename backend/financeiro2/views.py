from rest_framework import viewsets
from .models import Receita, Despesa, AnexoComprovante
from .serializers import ReceitaSerializer, DespesaSerializer, AnexoComprovanteSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

class AnexoComprovanteViewSet(viewsets.ModelViewSet):
    queryset = AnexoComprovante.objects.all()
    serializer_class = AnexoComprovanteSerializer 