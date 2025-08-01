from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    # Páginas principais
    path('', views.home, name='home'),
    path('planos/', views.planos, name='planos'),
    path('recursos/', views.recursos, name='recursos'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    
    # Páginas de vendas
    path('comparativo/', views.comparativo_planos, name='comparativo'),
    path('demo/', views.demo, name='demo'),
    
    # Páginas informativas
    path('blog/', views.blog, name='blog'),
    path('suporte/', views.suporte, name='suporte'),
    path('politica-privacidade/', views.politica_privacidade, name='politica_privacidade'),
    path('termos-uso/', views.termos_uso, name='termos_uso'),
    
    # APIs
    path('api/capturar-lead/', views.capturar_lead, name='capturar_lead'),
] 