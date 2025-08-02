from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
import json
import random
from datetime import datetime

from .models import ExperienciaAR, SessaoAR, ObjetoAR, InteracaoAR

@login_required
def ar_dashboard(request):
    """Dashboard principal da Realidade Aumentada"""
    
    context = {
        'experiencias': ExperienciaAR.objects.filter(ativo=True),
        'sessoes_recentes': SessaoAR.objects.filter(usuario=request.user)[:5],
        'objetos': ObjetoAR.objects.all()[:10],
        
        # Estatísticas simuladas
        'stats': {
            'experiencias_disponiveis': ExperienciaAR.objects.filter(ativo=True).count(),
            'sessoes_hoje': random.randint(10, 50),
            'objetos_3d': ObjetoAR.objects.count(),
            'tempo_medio_sessao': '8.5 minutos',
        }
    }
    
    return render(request, 'ar_experience/dashboard.html', context)

@login_required
def lista_experiencias(request):
    """Lista todas as experiências AR disponíveis"""
    
    experiencias = ExperienciaAR.objects.filter(ativo=True)
    
    context = {
        'experiencias': experiencias,
        'categorias': ExperienciaAR.TIPO_CHOICES
    }
    
    return render(request, 'ar_experience/lista_experiencias.html', context)

@login_required
def detalhes_experiencia(request, pk):
    """Detalhes de uma experiência AR específica"""
    
    experiencia = get_object_or_404(ExperienciaAR, pk=pk)
    
    # Criar objetos de exemplo se não existirem
    if not ObjetoAR.objects.exists():
        objetos_exemplo = [
            {
                'nome': 'Produto 3D Premium',
                'escala': 1.0,
                'posicao_x': 0.0,
                'posicao_y': 0.0,
                'posicao_z': 0.0,
            },
            {
                'nome': 'Estante Virtual',
                'escala': 1.5,
                'posicao_x': 2.0,
                'posicao_y': 0.0,
                'posicao_z': -1.0,
            },
            {
                'nome': 'Interface Holográfica',
                'escala': 0.8,
                'posicao_x': -1.0,
                'posicao_y': 1.5,
                'posicao_z': 0.0,
            }
        ]
        
        for obj in objetos_exemplo:
            ObjetoAR.objects.create(**obj)
    
    context = {
        'experiencia': experiencia,
        'objetos': ObjetoAR.objects.all(),
        'sessoes_usuario': SessaoAR.objects.filter(
            usuario=request.user, 
            experiencia=experiencia
        )[:5]
    }
    
    return render(request, 'ar_experience/detalhes_experiencia.html', context)

@login_required
def iniciar_sessao(request, pk):
    """Iniciar uma sessão AR"""
    
    experiencia = get_object_or_404(ExperienciaAR, pk=pk)
    
    # Criar nova sessão
    sessao = SessaoAR.objects.create(
        usuario=request.user,
        experiencia=experiencia
    )
    
    context = {
        'sessao': sessao,
        'experiencia': experiencia,
        'objetos': ObjetoAR.objects.all(),
        'marcador_ar': experiencia.marcador_ar.url if experiencia.marcador_ar else None
    }
    
    return render(request, 'ar_experience/sessao_ar.html', context)

@login_required
def lista_objetos(request):
    """Lista todos os objetos 3D disponíveis"""
    
    objetos = ObjetoAR.objects.all()
    
    context = {
        'objetos': objetos,
        'total_objetos': objetos.count()
    }
    
    return render(request, 'ar_experience/lista_objetos.html', context)

def api_interacao_ar(request):
    """API para registrar interações AR"""
    if request.method == 'POST':
        data = json.loads(request.body)
        
        sessao_id = data.get('sessao_id')
        objeto_id = data.get('objeto_id')
        tipo_interacao = data.get('tipo')
        dados = data.get('dados', {})
        
        try:
            sessao = SessaoAR.objects.get(id=sessao_id)
            objeto = ObjetoAR.objects.get(id=objeto_id) if objeto_id else None
            
            InteracaoAR.objects.create(
                sessao=sessao,
                objeto=objeto,
                tipo=tipo_interacao,
                dados_interacao=dados
            )
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}) 