from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def dashboard_view(request):
    """Dashboard principal do sistema"""
    return render(request, 'backend/dashboard.html', {
        'title': 'Dashboard - Sistema JAM',
        'modules': [
            {'name': 'Financeiro', 'url': '/sistema/financeiro/', 'icon': 'fas fa-dollar-sign', 'color': 'success'},
            {'name': 'Produtos', 'url': '/sistema/produtos/', 'icon': 'fas fa-box', 'color': 'primary'},
            {'name': 'Vendas', 'url': '/sistema/vendas/', 'icon': 'fas fa-shopping-cart', 'color': 'warning'},
            {'name': 'Clientes', 'url': '/sistema/clientes/', 'icon': 'fas fa-users', 'color': 'info'},
            {'name': 'Estoque', 'url': '/sistema/estoque/', 'icon': 'fas fa-warehouse', 'color': 'secondary'},
            {'name': 'Relatórios', 'url': '/sistema/relatorios/', 'icon': 'fas fa-chart-bar', 'color': 'dark'},
            {'name': 'IA Assistant', 'url': '/ai/', 'icon': 'fas fa-robot', 'color': 'primary'},
            {'name': 'Realidade Aumentada', 'url': '/ar/', 'icon': 'fas fa-vr-cardboard', 'color': 'info'},
        ]
    })

def financeiro_view(request):
    """Módulo Financeiro"""
    return render(request, 'backend/financeiro.html', {
        'title': 'Financeiro - Sistema JAM',
        'stats': {
            'receitas_mes': 'R$ 125.000',
            'despesas_mes': 'R$ 85.000',
            'lucro_mes': 'R$ 40.000',
            'contas_pagar': 'R$ 15.000',
            'contas_receber': 'R$ 35.000'
        }
    })

def produtos_view(request):
    """Módulo de Produtos"""
    return render(request, 'backend/produtos.html', {
        'title': 'Produtos - Sistema JAM',
        'stats': {
            'total_produtos': 1.250,
            'produtos_ativos': 1.180,
            'produtos_baixo_estoque': 45,
            'categorias': 25
        }
    })

def vendas_view(request):
    """Módulo de Vendas"""
    return render(request, 'backend/vendas.html', {
        'title': 'Vendas - Sistema JAM',
        'stats': {
            'vendas_hoje': 15,
            'vendas_mes': 450,
            'receita_hoje': 'R$ 8.500',
            'receita_mes': 'R$ 125.000',
            'ticket_medio': 'R$ 278'
        }
    })

def clientes_view(request):
    """Módulo de Clientes"""
    return render(request, 'backend/clientes.html', {
        'title': 'Clientes - Sistema JAM',
        'stats': {
            'total_clientes': 2.850,
            'clientes_ativos': 2.650,
            'novos_mes': 45,
            'satisfacao': '4.8/5'
        }
    })

def estoque_view(request):
    """Módulo de Estoque"""
    return render(request, 'backend/estoque.html', {
        'title': 'Estoque - Sistema JAM',
        'stats': {
            'total_itens': 15.250,
            'valor_estoque': 'R$ 450.000',
            'itens_baixo_estoque': 125,
            'itens_sem_estoque': 8
        }
    })

def relatorios_view(request):
    """Módulo de Relatórios"""
    return render(request, 'backend/relatorios.html', {
        'title': 'Relatórios - Sistema JAM',
        'reports': [
            'Relatório de Vendas',
            'Relatório Financeiro',
            'Relatório de Estoque',
            'Relatório de Clientes',
            'Relatório de Produtividade'
        ]
    })

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('financeiro/', financeiro_view, name='financeiro'),
    path('produtos/', produtos_view, name='produtos'),
    path('vendas/', vendas_view, name='vendas'),
    path('clientes/', clientes_view, name='clientes'),
    path('estoque/', estoque_view, name='estoque'),
    path('relatorios/', relatorios_view, name='relatorios'),
] 