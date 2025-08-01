from django.shortcuts import render
from rest_framework import viewsets
from .models import Deposito
from .serializers import DepositoSerializer

# Create your views here.

class DepositoViewSet(viewsets.ModelViewSet):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer

def lista_depositos(request):
    depositos = Deposito.objects.all()
    return render(request, 'depositos/lista.html', {'depositos': depositos})
