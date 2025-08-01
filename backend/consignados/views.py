from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count, Sum, Q
from django.utils import timezone
from datetime import timedelta
from .models import Consignado, HistoricoConsignado, NotificacaoWhatsApp
from backend.clientes.models import Cliente
from backend.lojas.models import Loja

@staff_member_required
def consignados_dashboard(request):
    """Dashboard principal de consignados"""
    # Estatísticas gerais
    total_consignados = Consignado.objects.count()
    em_venda = Consignado.objects.filter(status='em_venda').count()
    vendidos = Consignado.objects.filter(status='vendido').count()
    recebidos = Consignado.objects.filter(status='recebido').count()
    
    # Valores
    valor_total_venda = Consignado.objects.filter(status='vendido').aggregate(
        total=Sum('valor_venda')
    )['total'] or 0
    
    valor_total_repasse = Consignado.objects.filter(status='vendido').aggregate(
        total=Sum('valor_repasse')
    )['total'] or 0
    
    # Consignados por status
    consignados_por_status = Consignado.objects.values('status').annotate(
        total=Count('id')
    ).order_by('status')
    
    # Últimos consignados
    ultimos_consignados = Consignado.objects.select_related('cliente', 'loja').order_by('-data_recebimento')[:10]
    
    # Consignados que precisam de atenção
    consignados_antigos = Consignado.objects.filter(
        status='em_venda',
        data_recebimento__lte=timezone.now() - timedelta(days=30)
    ).select_related('cliente', 'loja')
    
    context = {
        'total_consignados': total_consignados,
        'em_venda': em_venda,
        'vendidos': vendidos,
        'recebidos': recebidos,
        'valor_total_venda': valor_total_venda,
        'valor_total_repasse': valor_total_repasse,
        'consignados_por_status': consignados_por_status,
        'ultimos_consignados': ultimos_consignados,
        'consignados_antigos': consignados_antigos,
    }
    
    return render(request, 'admin/consignados_dashboard.html', context)

@staff_member_required
def lista_consignados(request):
    """Lista todos os consignados com filtros"""
    status_filter = request.GET.get('status', '')
    loja_filter = request.GET.get('loja', '')
    cliente_filter = request.GET.get('cliente', '')
    
    consignados = Consignado.objects.select_related('cliente', 'loja', 'responsavel')
    
    if status_filter:
        consignados = consignados.filter(status=status_filter)
    if loja_filter:
        consignados = consignados.filter(loja_id=loja_filter)
    if cliente_filter:
        consignados = consignados.filter(
            Q(cliente__nome__icontains=cliente_filter) |
            Q(cliente__telefone__icontains=cliente_filter)
        )
    
    # Ordenação
    order_by = request.GET.get('order_by', '-data_recebimento')
    consignados = consignados.order_by(order_by)
    
    # Lojas para filtro
    lojas = Loja.objects.all()
    
    context = {
        'consignados': consignados,
        'lojas': lojas,
        'status_filter': status_filter,
        'loja_filter': loja_filter,
        'cliente_filter': cliente_filter,
    }
    
    return render(request, 'admin/lista_consignados.html', context)

@staff_member_required
def detalhes_consignado(request, consignado_id):
    """Detalhes de um consignado específico"""
    consignado = get_object_or_404(Consignado.objects.select_related('cliente', 'loja', 'responsavel'), id=consignado_id)
    historico = consignado.historico.all().order_by('-data_mudanca')
    notificacoes = consignado.notificacoes.all().order_by('-data_envio')
    
    context = {
        'consignado': consignado,
        'historico': historico,
        'notificacoes': notificacoes,
    }
    
    return render(request, 'admin/detalhes_consignado.html', context)

@staff_member_required
def alterar_status(request, consignado_id):
    """Altera o status de um consignado via AJAX"""
    if request.method == 'POST':
        consignado = get_object_or_404(Consignado, id=consignado_id)
        novo_status = request.POST.get('status')
        observacao = request.POST.get('observacao', '')
        
        if novo_status and novo_status in dict(Consignado.STATUS_CHOICES):
            status_anterior = consignado.status
            consignado.status = novo_status
            consignado.observacoes = observacao
            consignado.responsavel = request.user
            consignado.save()
            
            # Registrar no histórico
            HistoricoConsignado.objects.create(
                consignado=consignado,
                status_anterior=status_anterior,
                status_novo=novo_status,
                observacao=observacao,
                responsavel=request.user
            )
            
            # Enviar notificação WhatsApp se configurado
            if consignado.notificar_whatsapp and consignado.whatsapp_cliente:
                enviar_notificacao_whatsapp(consignado, novo_status, observacao)
            
            messages.success(request, f'Status alterado para: {consignado.get_status_display()}')
            return JsonResponse({'success': True, 'status': consignado.get_status_display()})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})

@staff_member_required
def relatorio_consignados(request):
    """Relatório detalhado de consignados"""
    # Filtros de data
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    
    consignados = Consignado.objects.select_related('cliente', 'loja')
    
    if data_inicio:
        consignados = consignados.filter(data_recebimento__date__gte=data_inicio)
    if data_fim:
        consignados = consignados.filter(data_recebimento__date__lte=data_fim)
    
    # Estatísticas
    total_recebidos = consignados.count()
    total_vendidos = consignados.filter(status='vendido').count()
    total_em_venda = consignados.filter(status='em_venda').count()
    
    # Valores
    valor_total_venda = consignados.filter(status='vendido').aggregate(
        total=Sum('valor_venda')
    )['total'] or 0
    
    valor_total_repasse = consignados.filter(status='vendido').aggregate(
        total=Sum('valor_repasse')
    )['total'] or 0
    
    # Por loja
    consignados_por_loja = consignados.values('loja__nome').annotate(
        total=Count('id'),
        vendidos=Count('id', filter=Q(status='vendido')),
        em_venda=Count('id', filter=Q(status='em_venda'))
    )
    
    # Por status
    consignados_por_status = consignados.values('status').annotate(
        total=Count('id')
    )
    
    context = {
        'total_recebidos': total_recebidos,
        'total_vendidos': total_vendidos,
        'total_em_venda': total_em_venda,
        'valor_total_venda': valor_total_venda,
        'valor_total_repasse': valor_total_repasse,
        'consignados_por_loja': consignados_por_loja,
        'consignados_por_status': consignados_por_status,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    }
    
    return render(request, 'admin/relatorio_consignados.html', context)

def enviar_notificacao_whatsapp(consignado, novo_status, observacao):
    """Envia notificação via WhatsApp"""
    try:
        # Aqui você integraria com a API do WhatsApp
        # Por enquanto, apenas registra a notificação
        mensagem = f"""
🔄 *Atualização do seu Consignado*

📦 *Produto:* {consignado.nome_produto}
🔢 *Código:* {consignado.codigo}
📊 *Status:* {consignado.get_status_display()}

📝 *Observação:* {observacao if observacao else 'Nenhuma'}

⏰ *Data:* {timezone.now().strftime('%d/%m/%Y %H:%M')}

Obrigado por confiar em nós! 🤝
        """.strip()
        
        NotificacaoWhatsApp.objects.create(
            consignado=consignado,
            tipo='status_change',
            mensagem=mensagem,
            telefone=consignado.whatsapp_cliente,
            enviado=True
        )
        
    except Exception as e:
        NotificacaoWhatsApp.objects.create(
            consignado=consignado,
            tipo='status_change',
            mensagem=mensagem,
            telefone=consignado.whatsapp_cliente,
            enviado=False,
            erro=str(e)
        ) 