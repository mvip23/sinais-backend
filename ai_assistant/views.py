from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
import random
from datetime import datetime, timedelta

from .models import AIAssistant, ConversaIA, PredicaoNegocio, AutomacaoIA

@login_required
def ai_dashboard(request):
    """Dashboard principal da IA"""
    
    # Dados simulados para demonstração
    context = {
        'assistentes': AIAssistant.objects.filter(ativo=True),
        'conversas_recentes': ConversaIA.objects.filter(usuario=request.user)[:5],
        'predicoes': PredicaoNegocio.objects.all()[:3],
        'automacoes': AutomacaoIA.objects.filter(ativo=True),
        
        # Estatísticas simuladas
        'stats': {
            'conversas_hoje': random.randint(50, 200),
            'predicoes_acuradas': random.randint(85, 98),
            'automacoes_ativas': AutomacaoIA.objects.filter(ativo=True).count(),
            'tempo_economizado': random.randint(10, 50),  # horas
        }
    }
    
    return render(request, 'ai_assistant/dashboard.html', context)

@csrf_exempt
def chat_ai(request):
    """Chat com IA"""
    if request.method == 'POST':
        data = json.loads(request.body)
        pergunta = data.get('pergunta', '')
        
        # Simular resposta da IA
        respostas = [
            "Analisando seus dados, posso sugerir otimizações no estoque...",
            "Baseado no histórico de vendas, recomendo focar nos produtos A e B...",
            "Detectei uma tendência de crescimento de 15% nas vendas online...",
            "Sua margem de lucro pode ser melhorada em 8% com as estratégias corretas...",
            "Identifiquei 3 oportunidades de redução de custos...",
        ]
        
        resposta = random.choice(respostas)
        
        # Salvar conversa
        if request.user.is_authenticated:
            assistente = AIAssistant.objects.filter(tipo='chatbot').first()
            if assistente:
                ConversaIA.objects.create(
                    usuario=request.user,
                    assistente=assistente,
                    pergunta=pergunta,
                    resposta=resposta
                )
        
        return JsonResponse({
            'resposta': resposta,
            'timestamp': datetime.now().isoformat()
        })
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@login_required
def analytics_preditivo(request):
    """Analytics preditivo com Machine Learning"""
    
    # Simular predições
    predicoes = {
        'vendas_proximos_30_dias': {
            'valor': random.randint(50000, 150000),
            'crescimento': random.randint(5, 25),
            'confianca': random.randint(85, 98)
        },
        'produtos_mais_vendidos': [
            {'nome': 'Produto A', 'quantidade': random.randint(100, 500)},
            {'nome': 'Produto B', 'quantidade': random.randint(80, 400)},
            {'nome': 'Produto C', 'quantidade': random.randint(60, 300)},
        ],
        'tendencias_mercado': [
            'Crescimento de 15% em vendas online',
            'Aumento de 8% na demanda por produtos premium',
            'Redução de 12% nos custos operacionais',
        ]
    }
    
    context = {
        'predicoes': predicoes,
        'historico_predicoes': PredicaoNegocio.objects.all()[:10]
    }
    
    return render(request, 'ai_assistant/analytics.html', context)

@login_required
def automacoes_inteligentes(request):
    """Automações inteligentes"""
    
    # Criar automações de exemplo se não existirem
    if not AutomacaoIA.objects.exists():
        automacoes_exemplo = [
            {
                'nome': 'Reabastecimento Automático',
                'descricao': 'Reabastece estoque automaticamente quando atinge nível mínimo',
                'trigger': 'Estoque baixo',
                'acao': 'Gerar pedido de compra'
            },
            {
                'nome': 'Alertas de Vendas',
                'descricao': 'Notifica sobre oportunidades de venda',
                'trigger': 'Cliente inativo há 30 dias',
                'acao': 'Enviar oferta personalizada'
            },
            {
                'nome': 'Análise de Risco',
                'descricao': 'Monitora riscos financeiros em tempo real',
                'trigger': 'Margem de lucro < 15%',
                'acao': 'Gerar relatório de alerta'
            }
        ]
        
        for auto in automacoes_exemplo:
            AutomacaoIA.objects.create(**auto)
    
    context = {
        'automacoes': AutomacaoIA.objects.filter(ativo=True),
        'logs_automacao': [
            {'acao': 'Reabastecimento automático executado', 'hora': '10:30'},
            {'acao': 'Análise de risco concluída', 'hora': '09:15'},
            {'acao': 'Alerta de vendas enviado', 'hora': '08:45'},
        ]
    }
    
    return render(request, 'ai_assistant/automacoes.html', context)

@login_required
def visao_computacional(request):
    """Visão computacional para análise de produtos"""
    
    context = {
        'analises': [
            {
                'produto': 'Produto A',
                'qualidade': '98%',
                'defeitos_detectados': 2,
                'status': 'Aprovado'
            },
            {
                'produto': 'Produto B', 
                'qualidade': '95%',
                'defeitos_detectados': 5,
                'status': 'Aprovado'
            },
            {
                'produto': 'Produto C',
                'qualidade': '87%',
                'defeitos_detectados': 13,
                'status': 'Rejeitado'
            }
        ],
        'estatisticas': {
            'produtos_analisados': random.randint(1000, 5000),
            'taxa_aprovacao': random.randint(85, 98),
            'tempo_medio_analise': '2.3 segundos'
        }
    }
    
    return render(request, 'ai_assistant/visao_computacional.html', context)
