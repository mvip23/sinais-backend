from django.contrib import admin
from .models import OrdemServico, ItemOrdemServico, CheckListOrdemServico

# Register your models here.
admin.site.register(OrdemServico)
admin.site.register(ItemOrdemServico)
admin.site.register(CheckListOrdemServico)

# Nenhuma configuração extra necessária aqui para templates customizados, pois o Django procura automaticamente por 'templates/admin/base_site.html' nos apps instalados.
