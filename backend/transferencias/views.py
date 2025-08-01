from django.shortcuts import render
from rest_framework import viewsets
from .models import TransferenciaEstoque
from .serializers import TransferenciaEstoqueSerializer

# Create your views here.

class TransferenciaEstoqueViewSet(viewsets.ModelViewSet):
    queryset = TransferenciaEstoque.objects.all()
    serializer_class = TransferenciaEstoqueSerializer
