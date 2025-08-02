from django.urls import path
from . import views

app_name = 'ai_assistant'

urlpatterns = [
    path('', views.ai_dashboard, name='dashboard'),
    path('chat/', views.chat_ai, name='chat'),
    path('analytics/', views.analytics_preditivo, name='analytics'),
    path('automacoes/', views.automacoes_inteligentes, name='automacoes'),
    path('visao-computacional/', views.visao_computacional, name='visao_computacional'),
] 