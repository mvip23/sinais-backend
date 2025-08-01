from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.db.models import Sum, Count, Avg
from datetime import datetime, timedelta
from backend.vendas.models import Venda
from backend.clientes.models import Cliente
from backend.ordens_servico.models import OrdemServico
from backend.produtos.models import Produto
from backend.estoque.models import Estoque
from backend.financeiro2.models import Receita, Despesa

@staff_member_required
def relatorios_dashboard(request):
    """Dashboard principal de relatórios"""
    context = {
        'total_vendas': Venda.objects.count(),
        'total_clientes': Cliente.objects.count(),
        'total_os': OrdemServico.objects.count(),
        'total_produtos': Produto.objects.count(),
    }
    return render(request, 'admin/relatorios_dashboard.html', context)

@staff_member_required
def relatorio_vendas(request):
    """Relatório de vendas"""
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    
    vendas = Venda.objects.all()
    
    if data_inicio:
        vendas = vendas.filter(data__date__gte=data_inicio)
    if data_fim:
        vendas = vendas.filter(data__date__lte=data_fim)
    
    # Estatísticas
    total_vendas = vendas.count()
    valor_total = vendas.aggregate(total=Sum('total'))['total'] or 0
    media_venda = vendas.aggregate(media=Avg('total'))['media'] or 0
    
    # Vendas por loja
    vendas_por_loja = vendas.values('loja__nome').annotate(
        total_vendas=Count('id'),
        valor_total=Sum('total')
    )
    
    context = {
        'vendas': vendas.order_by('-data')[:50],
        'total_vendas': total_vendas,
        'valor_total': valor_total,
        'media_venda': media_venda,
        'vendas_por_loja': vendas_por_loja,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    }
    
    return render(request, 'admin/relatorio_vendas.html', context)

@staff_member_required
def relatorio_estoque(request):
    """Relatório de estoque"""
    estoque_items = Estoque.objects.select_related('produto', 'deposito').all()
    
    # Produtos com baixo estoque (menos de 10 unidades)
    baixo_estoque = estoque_items.filter(quantidade__lt=10)
    
    # Total por depósito
    total_por_deposito = estoque_items.values('deposito__nome').annotate(
        total_produtos=Count('produto'),
        quantidade_total=Sum('quantidade')
    )
    
    context = {
        'estoque_items': estoque_items,
        'baixo_estoque': baixo_estoque,
        'total_por_deposito': total_por_deposito,
    }
    
    return render(request, 'admin/relatorio_estoque.html', context)

@staff_member_required
def relatorio_financeiro(request):
    """Relatório financeiro"""
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    
    receitas = Receita.objects.all()
    despesas = Despesa.objects.all()
    
    if data_inicio:
        receitas = receitas.filter(data__date__gte=data_inicio)
        despesas = despesas.filter(data__date__gte=data_inicio)
    if data_fim:
        receitas = receitas.filter(data__date__lte=data_fim)
        despesas = despesas.filter(data__date__lte=data_fim)
    
    total_receitas = receitas.aggregate(total=Sum('valor'))['total'] or 0
    total_despesas = despesas.aggregate(total=Sum('valor'))['total'] or 0
    saldo = total_receitas - total_despesas
    
    # Receitas por categoria
    receitas_por_categoria = receitas.values('categoria').annotate(
        total=Sum('valor'),
        quantidade=Count('id')
    )
    
    # Despesas por categoria
    despesas_por_categoria = despesas.values('categoria').annotate(
        total=Sum('valor'),
        quantidade=Count('id')
    )
    
    context = {
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo,
        'receitas_por_categoria': receitas_por_categoria,
        'despesas_por_categoria': despesas_por_categoria,
        'receitas': receitas.order_by('-data')[:20],
        'despesas': despesas.order_by('-data')[:20],
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    }
    
    return render(request, 'admin/relatorio_financeiro.html', context)

@staff_member_required
def api_dados_dashboard(request):
    """API para dados do dashboard"""
    # Últimos 30 dias
    data_inicio = datetime.now() - timedelta(days=30)
    
    # Vendas dos últimos 30 dias
    vendas_30_dias = Venda.objects.filter(data__gte=data_inicio).count()
    
    # Receitas dos últimos 30 dias
    receitas_30_dias = Receita.objects.filter(data__gte=data_inicio).aggregate(
        total=Sum('valor')
    )['total'] or 0
    
    # Despesas dos últimos 30 dias
    despesas_30_dias = Despesa.objects.filter(data__gte=data_inicio).aggregate(
        total=Sum('valor')
    )['total'] or 0
    
    # OS abertas
    os_abertas = OrdemServico.objects.filter(status='aberta').count()
    
    # Produtos com baixo estoque
    baixo_estoque = Estoque.objects.filter(quantidade__lt=10).count()
    
    return JsonResponse({
        'vendas_30_dias': vendas_30_dias,
        'receitas_30_dias': float(receitas_30_dias),
        'despesas_30_dias': float(despesas_30_dias),
        'os_abertas': os_abertas,
        'baixo_estoque': baixo_estoque,
    }) 