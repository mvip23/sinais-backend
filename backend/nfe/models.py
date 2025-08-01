from django.db import models
from backend.vendas.models import Venda

class NFe(models.Model):
    venda = models.OneToOneField(Venda, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    chave_acesso = models.CharField(max_length=44)
    xml = models.TextField()
    data_emissao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"NF-e {self.numero} - {self.venda}"
