from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Sum, Count, Q
from datetime import datetime, timedelta
from backend.ordens_servico.models import OrdemServico
from backend.clientes.models import Cliente
from backend.vendas.models import Venda
from backend.estoque.models import Estoque
from backend.financeiro2.models import Receita, Despesa
from backend.produtos.models import Produto

@staff_member_required
def dashboard_view(request):
    # Dados básicos
    total_os = OrdemServico.objects.count()
    total_clientes = Cliente.objects.count()
    total_vendas = Venda.objects.count()
    total_produtos = Produto.objects.count()
    
    # Dados dos últimos 30 dias
    data_30_dias = datetime.now() - timedelta(days=30)
    
    vendas_30_dias = Venda.objects.filter(data__gte=data_30_dias).count()
    receitas_30_dias = Receita.objects.filter(data__gte=data_30_dias).aggregate(
        total=Sum('valor')
    )['total'] or 0
    despesas_30_dias = Despesa.objects.filter(data__gte=data_30_dias).aggregate(
        total=Sum('valor')
    )['total'] or 0
    
    # Status das OS
    os_abertas = OrdemServico.objects.filter(status='aberta').count()
    os_em_andamento = OrdemServico.objects.filter(status='em_andamento').count()
    os_finalizadas = OrdemServico.objects.filter(status='finalizada').count()
    
    # Produtos com baixo estoque
    baixo_estoque = Estoque.objects.filter(quantidade__lt=10).count()
    
    # Top 5 produtos mais vendidos (simulado)
    produtos_mais_vendidos = Produto.objects.all()[:5]
    
    # Vendas por dia (últimos 7 dias)
    vendas_por_dia = []
    for i in range(7):
        data = datetime.now() - timedelta(days=i)
        vendas_dia = Venda.objects.filter(
            data__date=data.date()
        ).count()
        vendas_por_dia.append({
            'data': data.strftime('%d/%m'),
            'vendas': vendas_dia
        })
    vendas_por_dia.reverse()
    
    context = {
        'total_os': total_os,
        'total_clientes': total_clientes,
        'total_vendas': total_vendas,
        'total_produtos': total_produtos,
        'vendas_30_dias': vendas_30_dias,
        'receitas_30_dias': receitas_30_dias,
        'despesas_30_dias': despesas_30_dias,
        'saldo_30_dias': receitas_30_dias - despesas_30_dias,
        'os_abertas': os_abertas,
        'os_em_andamento': os_em_andamento,
        'os_finalizadas': os_finalizadas,
        'baixo_estoque': baixo_estoque,
        'produtos_mais_vendidos': produtos_mais_vendidos,
        'vendas_por_dia': vendas_por_dia,
    }
    return render(request, 'dashboard/dashboard.html', context)
