from django.shortcuts import render
from rest_framework import viewsets
from .models import Estoque
from .serializers import EstoqueSerializer

# Create your views here.

class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
