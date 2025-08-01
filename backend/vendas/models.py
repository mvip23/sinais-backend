from django.db import models
from backend.clientes.models import Cliente
from backend.produtos.models import Produto
from backend.lojas.models import Loja

class Venda(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda {self.id} - {self.loja.nome} - {self.data.date()}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto.nome} x {self.quantidade}"
