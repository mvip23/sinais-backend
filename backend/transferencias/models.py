from django.db import models
from backend.depositos.models import Deposito
from backend.produtos.models import Produto

# Create your models here.

class TransferenciaEstoque(models.Model):
    deposito_origem = models.ForeignKey(Deposito, on_delete=models.CASCADE, related_name='transferencias_saida')
    deposito_destino = models.ForeignKey(Deposito, on_delete=models.CASCADE, related_name='transferencias_entrada')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.produto.nome}: {self.quantidade} de {self.deposito_origem} para {self.deposito_destino}"
