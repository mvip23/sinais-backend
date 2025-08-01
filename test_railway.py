#!/usr/bin/env python3
"""
Script de teste para Railway
"""

import os
import sys

print("🔍 Testando configuração do Railway...")

# Verificar variáveis de ambiente
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE', 'NÃO DEFINIDA')}")
print(f"SECRET_KEY: {os.environ.get('SECRET_KEY', 'NÃO DEFINIDA')}")
print(f"DATABASE_URL: {os.environ.get('DATABASE_URL', 'NÃO DEFINIDA')}")

# Verificar se o Django pode ser importado
try:
    import django
    print("✅ Django importado com sucesso!")
    
    # Configurar Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empresa_nova.settings_railway')
    django.setup()
    print("✅ Django configurado com sucesso!")
    
    # Testar importação de modelos
    from django.contrib.auth.models import User
    print("✅ Modelos Django importados com sucesso!")
    
    # Testar conexão com banco
    try:
        User.objects.count()
        print("✅ Conexão com banco de dados OK!")
    except Exception as e:
        print(f"❌ Erro na conexão com banco: {e}")
    
except Exception as e:
    print(f"❌ Erro ao importar/configurar Django: {e}")
    sys.exit(1)

print("🎉 Teste concluído com sucesso!") 