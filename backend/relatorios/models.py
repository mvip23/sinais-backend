from django.db import models
from backend.empresas.models import Empresa
from django.contrib.auth.models import User

class Relatorio(models.Model):
    TIPO_CHOICES = [
        ('vendas', 'Relatório de Vendas'),
        ('estoque', 'Relatório de Estoque'),
        ('financeiro', 'Relatório Financeiro'),
        ('clientes', 'Relatório de Clientes'),
        ('os', 'Relatório de Ordens de Serviço'),
        ('produtos', 'Relatório de Produtos'),
    ]
    
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    filtros = models.JSONField(default=dict, blank=True)
    arquivo_gerado = models.FileField(upload_to='relatorios/', blank=True, null=True)
    data_geracao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.nome}"
    
    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios" 