from django.shortcuts import render
from rest_framework import viewsets
from .models import Loja
from .serializers import LojaSerializer

# Create your views here.

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer
