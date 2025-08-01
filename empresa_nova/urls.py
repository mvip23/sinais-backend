"""
URL configuration for empresa_nova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import dashboard_view
from django.shortcuts import redirect
from backend.depositos.views import lista_depositos
from django.shortcuts import render
from backend.financeiro2.models import Receita, Despesa
from django.views.decorators.csrf import csrf_exempt
from backend.financeiro2.models import Despesa, AnexoComprovante
from backend.relatorios.views import (
    relatorios_dashboard, relatorio_vendas, relatorio_estoque, 
    relatorio_financeiro, api_dados_dashboard
)
from backend.consignados.views import (
    consignados_dashboard, lista_consignados, detalhes_consignado,
    alterar_status, relatorio_consignados
)

def financeiro_view(request):
    receitas = Receita.objects.all().order_by('-data')[:10]
    despesas = Despesa.objects.all().order_by('-data')[:10]
    return render(request, 'admin/financeiro.html', {'receitas': receitas, 'despesas': despesas})

@csrf_exempt
def nova_despesa_view(request):
    from django.shortcuts import redirect
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        categoria = request.POST.get('categoria')
        empresa_id = request.POST.get('empresa_id')
        usuario_id = request.POST.get('usuario_id')
        despesa = Despesa.objects.create(
            descricao=descricao,
            valor=valor,
            data=data,
            categoria=categoria,
            empresa_id=empresa_id,
            usuario_id=usuario_id
        )
        if request.FILES.get('comprovante'):
            AnexoComprovante.objects.create(
                despesa=despesa,
                arquivo=request.FILES['comprovante']
            )
        return redirect('financeiro')
    return render(request, 'admin/nova_despesa.html')

urlpatterns = [
    # Website URLs
    path('', include('website.urls')),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # Sistema ERP
    path('sistema/', dashboard_view, name='dashboard'),
    path('sistema/depositos/', lista_depositos, name='lista_depositos'),
    path('sistema/financeiro/', financeiro_view, name='financeiro'),
]

urlpatterns += [
    path('financeiro/nova-despesa/', nova_despesa_view, name='nova_despesa'),
    path('relatorios/', relatorios_dashboard, name='relatorios_dashboard'),
    path('relatorios/vendas/', relatorio_vendas, name='relatorio_vendas'),
    path('relatorios/estoque/', relatorio_estoque, name='relatorio_estoque'),
    path('relatorios/financeiro/', relatorio_financeiro, name='relatorio_financeiro'),
    path('api/dashboard-dados/', api_dados_dashboard, name='api_dashboard_dados'),
    # URLs do módulo Consignados
    path('consignados/', consignados_dashboard, name='consignados_dashboard'),
    path('consignados/lista/', lista_consignados, name='lista_consignados'),
    path('consignados/<int:consignado_id>/', detalhes_consignado, name='detalhes_consignado'),
    path('consignados/<int:consignado_id>/alterar-status/', alterar_status, name='alterar_status'),
    path('consignados/relatorio/', relatorio_consignados, name='relatorio_consignados'),
]

# Media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
