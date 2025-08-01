from django.contrib import admin
from .models import Relatorio

@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'empresa', 'data_inicio', 'data_fim', 'data_geracao', 'usuario')
    list_filter = ('tipo', 'empresa', 'data_geracao')
    search_fields = ('nome', 'empresa__nome')
    readonly_fields = ('data_geracao', 'arquivo_gerado')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('empresa', 'tipo', 'nome', 'usuario')
        }),
        ('Período', {
            'fields': ('data_inicio', 'data_fim')
        }),
        ('Configurações', {
            'fields': ('filtros',)
        }),
        ('Resultado', {
            'fields': ('arquivo_gerado', 'data_geracao'),
            'classes': ('collapse',)
        }),
    ) 