from django.urls import path
from . import views

app_name = 'ar_experience'

urlpatterns = [
    path('', views.ar_dashboard, name='dashboard'),
    path('experiencias/', views.lista_experiencias, name='experiencias'),
    path('experiencia/<int:pk>/', views.detalhes_experiencia, name='detalhes_experiencia'),
    path('sessao/<int:pk>/', views.iniciar_sessao, name='iniciar_sessao'),
    path('objetos/', views.lista_objetos, name='objetos'),
] 