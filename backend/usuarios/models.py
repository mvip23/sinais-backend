from django.db import models
from backend.empresas.models import Empresa

class Usuario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
