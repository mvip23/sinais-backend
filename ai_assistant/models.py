from django.db import models
from django.contrib.auth.models import User

class AIAssistant(models.Model):
    """Assistente de IA para o Sistema JAM"""
    
    TIPO_CHOICES = [
        ('chatbot', 'Chatbot'),
        ('analytics', 'Analytics Preditivo'),
        ('automation', 'Automação'),
        ('vision', 'Visão Computacional'),
        ('nlp', 'Processamento de Linguagem Natural'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

class ConversaIA(models.Model):
    """Histórico de conversas com IA"""
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    assistente = models.ForeignKey(AIAssistant, on_delete=models.CASCADE)
    pergunta = models.TextField()
    resposta = models.TextField()
    contexto = models.JSONField(default=dict)
    data_conversa = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_conversa']

class PredicaoNegocio(models.Model):
    """Predições de negócio usando Machine Learning"""
    
    TIPO_PREDICAO = [
        ('vendas', 'Vendas'),
        ('estoque', 'Estoque'),
        ('financeiro', 'Financeiro'),
        ('clientes', 'Clientes'),
        ('tendencias', 'Tendências de Mercado'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_PREDICAO)
    dados_entrada = models.JSONField()
    predicao = models.JSONField()
    acuracia = models.FloatField()
    data_predicao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Predição {self.get_tipo_display()} - {self.data_predicao}"

class AutomacaoIA(models.Model):
    """Automações inteligentes"""
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    trigger = models.CharField(max_length=100)  # Evento que dispara
    acao = models.TextField()  # Ação a ser executada
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
