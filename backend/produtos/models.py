from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)
    codigo_barras = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=10, default='un')
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome 