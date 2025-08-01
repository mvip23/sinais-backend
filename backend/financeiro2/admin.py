from django.contrib import admin
from .models import Receita, Despesa, AnexoComprovante

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'empresa', 'usuario', 'categoria')
    search_fields = ('descricao', 'categoria')
    list_filter = ('empresa', 'categoria', 'data')

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'empresa', 'usuario', 'categoria')
    search_fields = ('descricao', 'categoria')
    list_filter = ('empresa', 'categoria', 'data')

@admin.register(AnexoComprovante)
class AnexoComprovanteAdmin(admin.ModelAdmin):
    list_display = ('despesa', 'arquivo', 'criado_em')
    search_fields = ('despesa__descricao',)
    list_filter = ('criado_em',) 