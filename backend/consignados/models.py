from django.db import models
from django.contrib.auth.models import User
from backend.clientes.models import Cliente
from backend.lojas.models import Loja
from django.utils import timezone
import uuid

class Consignado(models.Model):
    STATUS_CHOICES = [
        ('recebido', '📦 Recebido'),
        ('avaliado', '🔍 Em Avaliação'),
        ('aprovado', '✅ Aprovado'),
        ('em_venda', '💰 À Venda'),
        ('vendido', '🎉 Vendido'),
        ('rejeitado', '❌ Rejeitado'),
        ('devolvido', '↩️ Devolvido'),
    ]
    
    CONDICAO_CHOICES = [
        ('excelente', '⭐ Excelente'),
        ('muito_bom', '⭐⭐ Muito Bom'),
        ('bom', '⭐⭐⭐ Bom'),
        ('regular', '⭐⭐⭐⭐ Regular'),
        ('ruim', '⭐⭐⭐⭐⭐ Ruim'),
    ]
    
    # Informações básicas
    codigo = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='consignados')
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='consignados')
    
    # Produto
    nome_produto = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descricao = models.TextField()
    condicao = models.CharField(max_length=20, choices=CONDICAO_CHOICES, default='bom')
    
    # Valores
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_repasse = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentual_repasse = models.DecimalField(max_digits=5, decimal_places=2, default=70.00)  # 70% para o cliente
    
    # Status e controle
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='recebido')
    data_recebimento = models.DateTimeField(auto_now_add=True)
    data_avaliacao = models.DateTimeField(null=True, blank=True)
    data_aprovacao = models.DateTimeField(null=True, blank=True)
    data_venda = models.DateTimeField(null=True, blank=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    
    # Responsável
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Observações
    observacoes = models.TextField(blank=True)
    
    # WhatsApp
    whatsapp_cliente = models.CharField(max_length=20, blank=True)
    notificar_whatsapp = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Consignado"
        verbose_name_plural = "Consignados"
        ordering = ['-data_recebimento']
    
    def __str__(self):
        return f"{self.codigo} - {self.nome_produto} ({self.cliente.nome})"
    
    def save(self, *args, **kwargs):
        # Gerar código único se não existir
        if not self.codigo:
            self.codigo = f"CONS-{uuid.uuid4().hex[:8].upper()}"
        
        # Atualizar datas baseado no status
        if self.status == 'avaliado' and not self.data_avaliacao:
            self.data_avaliacao = timezone.now()
        elif self.status == 'aprovado' and not self.data_aprovacao:
            self.data_aprovacao = timezone.now()
        elif self.status == 'vendido' and not self.data_venda:
            self.data_venda = timezone.now()
        elif self.status == 'devolvido' and not self.data_devolucao:
            self.data_devolucao = timezone.now()
        
        super().save(*args, **kwargs)
    
    @property
    def tempo_em_loja(self):
        """Calcula o tempo que o produto está na loja"""
        if self.data_venda:
            return self.data_venda - self.data_recebimento
        return timezone.now() - self.data_recebimento
    
    @property
    def status_display(self):
        """Retorna o status com emoji"""
        return dict(self.STATUS_CHOICES).get(self.status, self.status)

class HistoricoConsignado(models.Model):
    """Histórico de mudanças de status para transparência"""
    consignado = models.ForeignKey(Consignado, on_delete=models.CASCADE, related_name='historico')
    status_anterior = models.CharField(max_length=20, blank=True)
    status_novo = models.CharField(max_length=20)
    observacao = models.TextField(blank=True)
    data_mudanca = models.DateTimeField(auto_now_add=True)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = "Histórico de Consignado"
        verbose_name_plural = "Históricos de Consignados"
        ordering = ['-data_mudanca']
    
    def __str__(self):
        return f"{self.consignado.codigo} - {self.status_anterior} → {self.status_novo}"

class NotificacaoWhatsApp(models.Model):
    """Registro de notificações enviadas via WhatsApp"""
    consignado = models.ForeignKey(Consignado, on_delete=models.CASCADE, related_name='notificacoes')
    tipo = models.CharField(max_length=50)  # 'status_change', 'venda', 'devolucao', etc.
    mensagem = models.TextField()
    telefone = models.CharField(max_length=20)
    data_envio = models.DateTimeField(auto_now_add=True)
    enviado = models.BooleanField(default=False)
    erro = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Notificação WhatsApp"
        verbose_name_plural = "Notificações WhatsApp"
        ordering = ['-data_envio']
    
    def __str__(self):
        return f"{self.consignado.codigo} - {self.tipo} ({self.data_envio.strftime('%d/%m/%Y %H:%M')})" 