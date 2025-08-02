from django.db import models
from django.contrib.auth.models import User

class ExperienciaAR(models.Model):
    """Experiências de Realidade Aumentada"""
    
    TIPO_CHOICES = [
        ('produto', 'Visualização de Produto'),
        ('estoque', 'Gestão de Estoque'),
        ('treinamento', 'Treinamento'),
        ('manutencao', 'Manutenção'),
        ('vendas', 'Vendas'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()
    modelo_3d = models.FileField(upload_to='ar_models/', blank=True, null=True)
    marcador_ar = models.ImageField(upload_to='ar_markers/', blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

class SessaoAR(models.Model):
    """Sessões de uso da Realidade Aumentada"""
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    experiencia = models.ForeignKey(ExperienciaAR, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(blank=True, null=True)
    duracao = models.IntegerField(blank=True, null=True)  # em segundos
    dados_interacao = models.JSONField(default=dict)
    
    class Meta:
        ordering = ['-data_inicio']

class ObjetoAR(models.Model):
    """Objetos 3D para Realidade Aumentada"""
    
    nome = models.CharField(max_length=100)
    modelo_3d = models.FileField(upload_to='ar_objects/')
    textura = models.ImageField(upload_to='ar_textures/', blank=True, null=True)
    escala = models.FloatField(default=1.0)
    posicao_x = models.FloatField(default=0.0)
    posicao_y = models.FloatField(default=0.0)
    posicao_z = models.FloatField(default=0.0)
    rotacao = models.JSONField(default=dict)
    animacao = models.JSONField(default=dict)
    
    def __str__(self):
        return self.nome

class InteracaoAR(models.Model):
    """Interações do usuário com objetos AR"""
    
    TIPO_INTERACAO = [
        ('toque', 'Toque'),
        ('gesto', 'Gesto'),
        ('voz', 'Comando de Voz'),
        ('movimento', 'Movimento'),
    ]
    
    sessao = models.ForeignKey(SessaoAR, on_delete=models.CASCADE)
    objeto = models.ForeignKey(ObjetoAR, on_delete=models.CASCADE, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_INTERACAO)
    dados_interacao = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp'] 