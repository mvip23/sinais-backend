from django.db import models
from backend.lojas.models import Loja

class Deposito(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='depositos')
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} - {self.loja.nome}"
