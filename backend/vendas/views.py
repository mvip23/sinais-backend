from django.shortcuts import render
from rest_framework import viewsets
from .models import Venda, ItemVenda
from .serializers import VendaSerializer, ItemVendaSerializer

# Create your views here.

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer
