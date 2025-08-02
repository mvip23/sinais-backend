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
            {'name': 'Ordem de Serviço', 'url': '/sistema/ordem-servico/', 'icon': 'fas fa-tools', 'color': 'danger'},
            {'name': 'Gestão Pessoal', 'url': '/sistema/gestao-pessoal/', 'icon': 'fas fa-home', 'color': 'info'},
            {'name': 'Configurações', 'url': '/sistema/configuracoes/', 'icon': 'fas fa-cog', 'color': 'dark'},
            {'name': 'IA Assistant', 'url': '/ai/', 'icon': 'fas fa-robot', 'color': 'primary'},
            {'name': 'Realidade Aumentada', 'url': '/ar/', 'icon': 'fas fa-vr-cardboard', 'color': 'info'},
        ],
        'wizard_available': True
    })

def wizard_setup_view(request):
    """Wizard de configuração inicial da empresa"""
    step = request.GET.get('step', '1')
    
    if step == '1':
        return render(request, 'backend/wizard_step1.html', {
            'title': 'Setup da Empresa - Passo 1',
            'step': 1,
            'total_steps': 4,
            'progress': 25
        })
    elif step == '2':
        return render(request, 'backend/wizard_step2.html', {
            'title': 'Setup da Empresa - Passo 2',
            'step': 2,
            'total_steps': 4,
            'progress': 50
        })
    elif step == '3':
        return render(request, 'backend/wizard_step3.html', {
            'title': 'Setup da Empresa - Passo 3',
            'step': 3,
            'total_steps': 4,
            'progress': 75
        })
    elif step == '4':
        return render(request, 'backend/wizard_step4.html', {
            'title': 'Setup da Empresa - Passo 4',
            'step': 4,
            'total_steps': 4,
            'progress': 100
        })
    else:
        return render(request, 'backend/wizard_complete.html', {
            'title': 'Setup Concluído!',
            'empresa': {
                'nome': 'Sua Empresa',
                'cnpj': '12.345.678/0001-90',
                'endereco': 'Rua das Inovações, 123 - São Paulo, SP',
                'telefone': '(11) 99999-9999',
                'email': 'contato@suaempresa.com.br',
                'website': 'www.suaempresa.com.br'
            }
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

def ordem_servico_view(request):
    """Módulo de Ordem de Serviço"""
    return render(request, 'backend/ordem_servico.html', {
        'title': 'Ordem de Serviço - Sistema JAM',
        'ordens': [
            {
                'id': 'OS-001',
                'cliente': 'João Silva',
                'servico': 'Manutenção de Computador',
                'status': 'Em Andamento',
                'valor': 'R$ 150,00',
                'data': '02/08/2024'
            },
            {
                'id': 'OS-002',
                'cliente': 'Maria Santos',
                'servico': 'Instalação de Software',
                'status': 'Concluído',
                'valor': 'R$ 80,00',
                'data': '01/08/2024'
            },
            {
                'id': 'OS-003',
                'cliente': 'Pedro Costa',
                'servico': 'Limpeza de Sistema',
                'status': 'Aguardando',
                'valor': 'R$ 120,00',
                'data': '02/08/2024'
            }
        ]
    })

def gestao_pessoal_view(request):
    """Módulo de Gestão Pessoal Gratuita"""
    return render(request, 'backend/gestao_pessoal.html', {
        'title': 'Gestão Pessoal - Sistema JAM',
        'stats': {
            'despesas_mes': 'R$ 3.500',
            'receitas_mes': 'R$ 5.200',
            'saldo_mes': 'R$ 1.700',
            'contas_pendentes': 'R$ 850',
            'economias': 'R$ 2.300'
        },
        'despesas_domesticas': [
            {'categoria': 'Alimentação', 'valor': 'R$ 800', 'status': 'Pago'},
            {'categoria': 'Energia', 'valor': 'R$ 150', 'status': 'Pendente'},
            {'categoria': 'Água', 'valor': 'R$ 80', 'status': 'Pago'},
            {'categoria': 'Internet', 'valor': 'R$ 120', 'status': 'Pendente'},
            {'categoria': 'Aluguel', 'valor': 'R$ 1.200', 'status': 'Pago'}
        ],
        'contas_pessoais': [
            {'descricao': 'Cartão de Crédito', 'valor': 'R$ 450', 'vencimento': '15/08/2024', 'status': 'Pendente'},
            {'descricao': 'Seguro Carro', 'valor': 'R$ 180', 'vencimento': '20/08/2024', 'status': 'Pendente'},
            {'descricao': 'Academia', 'valor': 'R$ 89', 'vencimento': '10/08/2024', 'status': 'Pago'},
            {'descricao': 'Netflix', 'valor': 'R$ 39', 'vencimento': '05/08/2024', 'status': 'Pago'}
        ],
        'carro_combustivel': [
            {'tipo': 'Gasolina', 'valor': 'R$ 200', 'data': '01/08/2024', 'km': '45.250'},
            {'tipo': 'Óleo', 'valor': 'R$ 45', 'data': '15/07/2024', 'km': '44.800'},
            {'tipo': 'Manutenção', 'valor': 'R$ 350', 'data': '10/07/2024', 'km': '44.500'}
        ],
        'despesas_escolares': [
            {'item': 'Mensalidade', 'valor': 'R$ 450', 'status': 'Pago'},
            {'item': 'Material Escolar', 'valor': 'R$ 120', 'status': 'Pendente'},
            {'item': 'Uniforme', 'valor': 'R$ 85', 'status': 'Pago'},
            {'item': 'Transporte', 'valor': 'R$ 180', 'status': 'Pendente'}
        ]
    })

def configuracoes_view(request):
    """Módulo de Configurações Unificado"""
    return render(request, 'backend/configuracoes.html', {
        'title': 'Configurações - Sistema JAM',
        'empresa': {
            'nome': 'Sistema JAM',
            'cnpj': '12.345.678/0001-90',
            'endereco': 'Rua das Inovações, 123 - São Paulo, SP',
            'telefone': '(11) 99999-9999',
            'email': 'contato@sistemajam.com.br',
            'website': 'www.sistemajam.com.br',
            'logo': '/static/images/logo.png'
        },
        'usuarios': [
            {'nome': 'Admin Master', 'email': 'admin@sistemajam.com.br', 'nivel': 'Administrador'},
            {'nome': 'João Silva', 'email': 'joao@sistemajam.com.br', 'nivel': 'Gerente'},
            {'nome': 'Maria Santos', 'email': 'maria@sistemajam.com.br', 'nivel': 'Operador'}
        ],
        'relatorios': [
            'Relatório de Vendas',
            'Relatório Financeiro',
            'Relatório de Estoque',
            'Relatório de Clientes',
            'Relatório de Produtividade',
            'Relatório de Ordens de Serviço'
        ],
        'configuracoes_voz': {
            'ativo': True,
            'idioma': 'Português',
            'velocidade': 'Normal',
            'comandos_ativos': ['Nova venda', 'Buscar cliente', 'Gerar relatório', 'Abrir estoque']
        }
    })

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('wizard/', wizard_setup_view, name='wizard_setup'),
    path('financeiro/', financeiro_view, name='financeiro'),
    path('produtos/', produtos_view, name='produtos'),
    path('vendas/', vendas_view, name='vendas'),
    path('clientes/', clientes_view, name='clientes'),
    path('estoque/', estoque_view, name='estoque'),
    path('ordem-servico/', ordem_servico_view, name='ordem_servico'),
    path('gestao-pessoal/', gestao_pessoal_view, name='gestao_pessoal'),
    path('configuracoes/', configuracoes_view, name='configuracoes'),
] 