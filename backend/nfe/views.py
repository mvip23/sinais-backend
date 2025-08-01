from django.shortcuts import render
from rest_framework import viewsets
from .models import NFe
from .serializers import NFeSerializer

# Create your views here.

class NFeViewSet(viewsets.ModelViewSet):
    queryset = NFe.objects.all()
    serializer_class = NFeSerializer
