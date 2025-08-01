from django.db import models
from backend.clientes.models import Cliente
from backend.lojas.models import Loja
from backend.produtos.models import Produto

STATUS_CHOICES = [
    ('aberta', 'Aberta'),
    ('em_andamento', 'Em andamento'),
    ('finalizada', 'Finalizada'),
    ('cancelada', 'Cancelada'),
]

class OrdemServico(models.Model):
    """Representa uma ordem de serviço vinculada a um cliente e loja."""
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, verbose_name="Loja")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    descricao = models.TextField("Descrição do problema/serviço")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='aberta', verbose_name="Status")
    data_abertura = models.DateTimeField(auto_now_add=True, verbose_name="Data de abertura")
    data_fechamento = models.DateTimeField(null=True, blank=True, verbose_name="Data de fechamento")
    serial_number = models.CharField(max_length=100, blank=True, null=True, unique=False, verbose_name="Serial Number")
    foto_produto = models.ImageField(upload_to='os_fotos/', blank=True, null=True, verbose_name="Foto do Produto")
    termo_garantia = models.TextField(blank=True, null=True, default="O serviço realizado possui garantia de 90 dias, conforme legislação vigente, desde que o lacre e o serial estejam intactos.", verbose_name="Termo de Garantia")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    def __str__(self):
        return f"OS #{self.id} - {self.cliente.nome}"

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"
        constraints = [
            models.UniqueConstraint(
                fields=['serial_number'],
                condition=~models.Q(serial_number=None),
                name='unique_serial_number_not_null'
            )
        ]

class ItemOrdemServico(models.Model):
    """Itens/produtos vinculados a uma ordem de serviço."""
    ordem_servico = models.ForeignKey(OrdemServico, related_name='itens', on_delete=models.CASCADE, verbose_name="Ordem de Serviço")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name="Produto")
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantidade")
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Unitário")

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.produto.nome} x {self.quantidade}"

    class Meta:
        verbose_name = "Item da Ordem de Serviço"
        verbose_name_plural = "Itens da Ordem de Serviço"

class CheckListOrdemServico(models.Model):
    """Checklist de etapas ou itens a serem verificados em uma ordem de serviço."""
    ordem_servico = models.ForeignKey(OrdemServico, related_name='checklist', on_delete=models.CASCADE, verbose_name="Ordem de Serviço")
    item = models.CharField(max_length=255, verbose_name="Item do Checklist")
    realizado = models.BooleanField(default=False, verbose_name="Realizado")

    def __str__(self):
        return f"{self.item} - {'OK' if self.realizado else 'Pendente'}"

    class Meta:
        verbose_name = "Checklist da Ordem de Serviço"
        verbose_name_plural = "Checklists das Ordens de Serviço"
