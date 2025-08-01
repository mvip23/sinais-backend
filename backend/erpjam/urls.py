"""
URL configuration for erpjam project.

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
from rest_framework import routers
from empresas.views import EmpresaViewSet
from lojas.views import LojaViewSet
from depositos.views import DepositoViewSet
from produtos.views import ProdutoViewSet
from estoque.views import EstoqueViewSet
from transferencias.views import TransferenciaEstoqueViewSet
from usuarios.views import UsuarioViewSet
from clientes.views import ClienteViewSet
from vendas.views import VendaViewSet, ItemVendaViewSet
from nfe.views import NFeViewSet
from financeiro2.views import ReceitaViewSet, DespesaViewSet, AnexoComprovanteViewSet

router = routers.DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'lojas', LojaViewSet)
router.register(r'depositos', DepositoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'estoque', EstoqueViewSet)
router.register(r'transferencias', TransferenciaEstoqueViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'itens-venda', ItemVendaViewSet)
router.register(r'nfe', NFeViewSet)
router.register(r'receitas', ReceitaViewSet)
router.register(r'despesas', DespesaViewSet)
router.register(r'anexos-comprovante', AnexoComprovanteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/', include(router.urls)),
]
