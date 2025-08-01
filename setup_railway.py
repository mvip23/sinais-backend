#!/usr/bin/env python3
"""
Script de setup para Railway
Execute este script manualmente após o deploy
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empresa_nova.settings_railway')
django.setup()

from django.core.management import execute_from_command_line

def main():
    print("🚀 Iniciando setup do Sistema JAM...")
    
    try:
        # Executar migrações
        print("🔄 Executando migrações...")
        execute_from_command_line(['manage.py', 'migrate'])
        print("✅ Migrações concluídas!")
        
        # Criar superusuário
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            print("👤 Criando superusuário...")
            User.objects.create_superuser('admin', 'admin@sistemajam.com.br', 'SistemaJam2024!')
            print("✅ Superusuário criado: admin / SistemaJam2024!")
        else:
            print("✅ Superusuário já existe!")
        
        # Criar dados iniciais
        try:
            from website.models import ConfiguracaoSite, Plano, Beneficio
            
            if not ConfiguracaoSite.objects.exists():
                print("🌐 Criando configuração do site...")
                ConfiguracaoSite.objects.create(
                    titulo="Sistema JAM - ERP Mais Moderno do Mundo",
                    subtitulo="Transforme sua empresa com tecnologia de ponta",
                    descricao="O ERP mais inovador do mercado com IA, Realidade Aumentada e muito mais!",
                    email_contato="contato@sistemajam.com.br",
                    telefone="(11) 99999-9999",
                    endereco="São Paulo, SP - Brasil"
                )
                print("✅ Configuração do site criada!")
            
            if not Plano.objects.exists():
                print("💼 Criando planos...")
                # Planos
                Plano.objects.create(nome="Básico", preco=99.00, descricao="Ideal para pequenas empresas", destaque=False)
                Plano.objects.create(nome="Profissional", preco=199.00, descricao="Perfeito para empresas em crescimento", destaque=True)
                Plano.objects.create(nome="Enterprise", preco=399.00, descricao="Para grandes corporações", destaque=False)
                print("✅ Planos criados!")
            
            if not Beneficio.objects.exists():
                print("🎯 Criando benefícios...")
                beneficios = [
                    "Gestão completa de vendas",
                    "Controle de estoque", 
                    "Relatórios avançados",
                    "Suporte 24/7",
                    "Integração com APIs",
                    "Backup automático",
                    "IA Assistente",
                    "Realidade Aumentada"
                ]
                
                for beneficio in beneficios:
                    Beneficio.objects.create(
                        nome=beneficio,
                        descricao=f"Benefício: {beneficio}",
                        icone="fas fa-check"
                    )
                print("✅ Benefícios criados!")
                
        except Exception as e:
            print(f"⚠️ Erro ao criar dados iniciais: {e}")
        
        print("🎉 Setup concluído com sucesso!")
        print("🌐 Acesse: https://web-production-b885.up.railway.app")
        print("🔑 Login: admin / SistemaJam2024!")
        
    except Exception as e:
        print(f"❌ Erro durante setup: {e}")
        print("🔍 Verifique os logs para mais detalhes")

if __name__ == '__main__':
    main() 