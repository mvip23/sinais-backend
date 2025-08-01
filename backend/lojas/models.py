from django.db import models
from backend.empresas.models import Empresa

class Loja(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='lojas')
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.empresa.nome})"
