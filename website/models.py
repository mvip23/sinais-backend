from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Plano(models.Model):
    """Modelo para os planos de assinatura do ERP"""
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    preco_anual = models.DecimalField(max_digits=10, decimal_places=2)
    destaque = models.BooleanField(default=False)
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    # Limites do plano
    max_usuarios = models.IntegerField(default=1)
    max_empresas = models.IntegerField(default=1)
    max_produtos = models.IntegerField(default=100)
    max_clientes = models.IntegerField(default=100)
    
    # Funcionalidades incluídas
    tem_estoque = models.BooleanField(default=True)
    tem_vendas = models.BooleanField(default=True)
    tem_financeiro = models.BooleanField(default=True)
    tem_ordens_servico = models.BooleanField(default=True)
    tem_relatorios = models.BooleanField(default=True)
    tem_ia_assistant = models.BooleanField(default=False)
    tem_api = models.BooleanField(default=False)
    tem_suporte_prioritario = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['ordem', 'preco_mensal']
    
    def __str__(self):
        return self.nome
    
    @property
    def economia_anual(self):
        """Calcula a economia ao pagar anualmente"""
        return (self.preco_mensal * 12) - self.preco_anual

class Beneficio(models.Model):
    """Benefícios incluídos nos planos"""
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, help_text="Nome do ícone (ex: fa-chart-line)")
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['ordem']
    
    def __str__(self):
        return self.titulo

class Depoimento(models.Model):
    """Depoimentos de clientes"""
    nome = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='depoimentos/', blank=True, null=True)
    depoimento = models.TextField()
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_criacao']
    
    def __str__(self):
        return f"{self.nome} - {self.empresa}"

class Contato(models.Model):
    """Formulário de contato"""
    ASSUNTO_CHOICES = [
        ('vendas', 'Vendas'),
        ('suporte', 'Suporte'),
        ('parceria', 'Parceria'),
        ('outro', 'Outro'),
    ]
    
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True)
    empresa = models.CharField(max_length=100, blank=True)
    assunto = models.CharField(max_length=20, choices=ASSUNTO_CHOICES)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    respondido = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-data_envio']
    
    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Lead(models.Model):
    """Leads capturados no site"""
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100, blank=True)
    empresa = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    fonte = models.CharField(max_length=50, default='site')
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_cadastro']
    
    def __str__(self):
        return self.email

class ConfiguracaoSite(models.Model):
    """Configurações gerais do site"""
    titulo_site = models.CharField(max_length=100, default="Sistema JAM - ERP Moderno")
    subtitulo_site = models.CharField(max_length=200, default="O ERP mais moderno do mundo")
    descricao_site = models.TextField(default="Sistema completo para gestão empresarial")
    email_contato = models.EmailField(default="contato@sistemajam.com.br")
    telefone_contato = models.CharField(max_length=20, default="(11) 99999-9999")
    endereco = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    
    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configurações do Site"
    
    def __str__(self):
        return "Configurações do Site"
