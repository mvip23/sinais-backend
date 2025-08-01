from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Plano, Beneficio, Depoimento, Contato, Lead, ConfiguracaoSite
from .forms import ContatoForm, LeadForm
import json

def home(request):
    """Página inicial do site"""
    context = {
        'planos': Plano.objects.filter(ativo=True),
        'beneficios': Beneficio.objects.filter(ativo=True),
        'depoimentos': Depoimento.objects.filter(ativo=True)[:6],
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/home.html', context)

def planos(request):
    """Página de planos e preços"""
    context = {
        'planos': Plano.objects.filter(ativo=True),
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/planos.html', context)

def recursos(request):
    """Página de recursos e funcionalidades"""
    context = {
        'beneficios': Beneficio.objects.filter(ativo=True),
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/recursos.html', context)

def sobre(request):
    """Página sobre a empresa"""
    context = {
        'depoimentos': Depoimento.objects.filter(ativo=True),
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/sobre.html', context)

def contato(request):
    """Página de contato"""
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()
            
            # Enviar email de notificação
            try:
                send_mail(
                    f'Novo contato: {contato.assunto}',
                    f'''
                    Nome: {contato.nome}
                    Email: {contato.email}
                    Telefone: {contato.telefone}
                    Empresa: {contato.empresa}
                    Assunto: {contato.assunto}
                    Mensagem: {contato.mensagem}
                    ''',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Erro ao enviar email: {e}")
            
            messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
            return redirect('website:contato')
    else:
        form = ContatoForm()
    
    context = {
        'form': form,
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/contato.html', context)

@csrf_exempt
def capturar_lead(request):
    """API para capturar leads"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            nome = data.get('nome', '')
            empresa = data.get('empresa', '')
            telefone = data.get('telefone', '')
            fonte = data.get('fonte', 'site')
            
            if email:
                lead, created = Lead.objects.get_or_create(
                    email=email,
                    defaults={
                        'nome': nome,
                        'empresa': empresa,
                        'telefone': telefone,
                        'fonte': fonte
                    }
                )
                
                if created:
                    # Enviar email de boas-vindas
                    try:
                        send_mail(
                            'Bem-vindo ao Sistema JAM!',
                            f'''
                            Olá {nome or 'Visitante'}!
                            
                            Obrigado por se interessar pelo Sistema JAM!
                            Em breve entraremos em contato com mais informações.
                            
                            Atenciosamente,
                            Equipe Sistema JAM
                            ''',
                            settings.DEFAULT_FROM_EMAIL,
                            [email],
                            fail_silently=False,
                        )
                    except Exception as e:
                        print(f"Erro ao enviar email: {e}")
                
                return JsonResponse({'success': True, 'message': 'Lead capturado com sucesso!'})
            else:
                return JsonResponse({'success': False, 'message': 'Email é obrigatório'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Método não permitido'})

def comparativo_planos(request):
    """Página de comparação de planos"""
    context = {
        'planos': Plano.objects.filter(ativo=True),
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/comparativo.html', context)

def demo(request):
    """Página para agendar demonstração"""
    context = {
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/demo.html', context)

def blog(request):
    """Página do blog (futuro)"""
    context = {
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/blog.html', context)

def suporte(request):
    """Página de suporte"""
    context = {
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/suporte.html', context)

def politica_privacidade(request):
    """Página de política de privacidade"""
    context = {
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/politica-privacidade.html', context)

def termos_uso(request):
    """Página de termos de uso"""
    context = {
        'config': ConfiguracaoSite.objects.first(),
    }
    return render(request, 'website/termos-uso.html', context)
