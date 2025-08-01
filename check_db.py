#!/usr/bin/env python3
"""
Script para verificar conexão com banco de dados
"""

import os

print("🔍 Verificando variáveis de ambiente...")
print(f"DATABASE_URL: {os.environ.get('DATABASE_URL', 'NÃO DEFINIDA')}")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE', 'NÃO DEFINIDA')}")
print(f"SECRET_KEY: {os.environ.get('SECRET_KEY', 'NÃO DEFINIDA')}")

# Verificar se DATABASE_URL existe
if not os.environ.get('DATABASE_URL'):
    print("❌ DATABASE_URL não encontrada!")
    print("💡 Verifique se o banco PostgreSQL está conectado ao serviço web no Railway")
else:
    print("✅ DATABASE_URL encontrada!") 