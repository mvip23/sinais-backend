#!/usr/bin/env python3
"""
Script para executar migrações no Railway
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empresa_nova.settings_railway')
django.setup()

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    print("🔄 Executando migrações...")
    
    # Executar migrações
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Criar superusuário se não existir
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        print("👤 Criando superusuário...")
        User.objects.create_superuser('admin', 'admin@sistemajam.com.br', 'SistemaJam2024!')
        print("✅ Superusuário criado: admin / SistemaJam2024!")
    
    # Criar dados iniciais do site
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
    
    if not Plano.objects.exists():
        print("💼 Criando planos...")
        # Plano Básico
        plano_basico = Plano.objects.create(
            nome="Básico",
            preco=99.00,
            descricao="Ideal para pequenas empresas",
            destaque=False
        )
        
        # Plano Profissional
        plano_pro = Plano.objects.create(
            nome="Profissional",
            preco=199.00,
            descricao="Perfeito para empresas em crescimento",
            destaque=True
        )
        
        # Plano Enterprise
        plano_enterprise = Plano.objects.create(
            nome="Enterprise",
            preco=399.00,
            descricao="Para grandes corporações",
            destaque=False
        )
        
        # Benefícios
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
    
    print("✅ Configuração inicial concluída!") 