from django.db import models
from backend.produtos.models import Produto
from backend.depositos.models import Deposito

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ('produto', 'deposito')

    def __str__(self):
        return f"{self.produto.nome} - {self.deposito.nome}: {self.quantidade}"
