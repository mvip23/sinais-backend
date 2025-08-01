from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Consignado, HistoricoConsignado, NotificacaoWhatsApp

@admin.register(Consignado)
class ConsignadoAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'nome_produto', 'cliente', 'loja', 'status_display', 
        'valor_estimado', 'valor_venda', 'data_recebimento', 'tempo_em_loja_display'
    ]
    list_filter = [
        'status', 'condicao', 'loja', 'data_recebimento', 'responsavel'
    ]
    search_fields = [
        'codigo', 'nome_produto', 'marca', 'modelo', 'cliente__nome', 'cliente__telefone'
    ]
    readonly_fields = [
        'codigo', 'data_recebimento', 'data_avaliacao', 'data_aprovacao', 
        'data_venda', 'data_devolucao', 'tempo_em_loja_display'
    ]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo', 'cliente', 'loja', 'responsavel')
        }),
        ('Produto', {
            'fields': ('nome_produto', 'marca', 'modelo', 'descricao', 'condicao')
        }),
        ('Valores', {
            'fields': ('valor_estimado', 'valor_venda', 'percentual_repasse', 'valor_repasse')
        }),
        ('Status e Controle', {
            'fields': ('status', 'observacoes')
        }),
        ('WhatsApp', {
            'fields': ('whatsapp_cliente', 'notificar_whatsapp'),
            'classes': ('collapse',)
        }),
        ('Datas', {
            'fields': ('data_recebimento', 'data_avaliacao', 'data_aprovacao', 'data_venda', 'data_devolucao'),
            'classes': ('collapse',)
        }),
    )
    
    def status_display(self, obj):
        """Exibe o status com cores"""
        colors = {
            'recebido': '#17a2b8',
            'avaliado': '#ffc107',
            'aprovado': '#28a745',
            'em_venda': '#007bff',
            'vendido': '#6f42c1',
            'rejeitado': '#dc3545',
            'devolvido': '#6c757d'
        }
        color = colors.get(obj.status, '#6c757d')
        return format_html(
            '<span style="color: white; background-color: {}; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{}</span>',
            color, obj.status_display
        )
    status_display.short_description = 'Status'
    
    def tempo_em_loja_display(self, obj):
        """Exibe o tempo em loja de forma amigável"""
        tempo = obj.tempo_em_loja
        dias = tempo.days
        if dias == 0:
            return "Hoje"
        elif dias == 1:
            return "1 dia"
        else:
            return f"{dias} dias"
    tempo_em_loja_display.short_description = 'Tempo em Loja'
    
    def save_model(self, request, obj, form, change):
        """Salva o modelo e registra mudanças no histórico"""
        if change:  # Se é uma edição
            old_obj = Consignado.objects.get(pk=obj.pk)
            if old_obj.status != obj.status:
                HistoricoConsignado.objects.create(
                    consignado=obj,
                    status_anterior=old_obj.status,
                    status_novo=obj.status,
                    responsavel=request.user
                )
        super().save_model(request, obj, form, change)

@admin.register(HistoricoConsignado)
class HistoricoConsignadoAdmin(admin.ModelAdmin):
    list_display = [
        'consignado', 'status_anterior', 'status_novo', 'responsavel', 'data_mudanca'
    ]
    list_filter = ['status_novo', 'data_mudanca', 'responsavel']
    search_fields = ['consignado__codigo', 'consignado__nome_produto']
    readonly_fields = ['data_mudanca']
    
    def has_add_permission(self, request):
        return False  # Histórico é criado automaticamente

@admin.register(NotificacaoWhatsApp)
class NotificacaoWhatsAppAdmin(admin.ModelAdmin):
    list_display = [
        'consignado', 'tipo', 'telefone', 'enviado', 'data_envio'
    ]
    list_filter = ['tipo', 'enviado', 'data_envio']
    search_fields = ['consignado__codigo', 'telefone', 'mensagem']
    readonly_fields = ['data_envio']
    
    def has_add_permission(self, request):
        return False  # Notificações são criadas automaticamente 