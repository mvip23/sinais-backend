from django.shortcuts import render
from rest_framework import viewsets
from .models import Empresa
from .serializers import EmpresaSerializer

# Create your views here.

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
