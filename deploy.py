#!/usr/bin/env python3
"""
Script de Deploy Automatizado para Sistema JAM
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Executa um comando e mostra o progresso"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Concluído!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro em {description}: {e}")
        print(f"Erro: {e.stderr}")
        return False

def create_production_files():
    """Cria arquivos necessários para produção"""
    print("\n📁 Criando arquivos de produção...")
    
    # Criar diretório static se não existir
    static_dir = Path("static")
    static_dir.mkdir(exist_ok=True)
    
    # Criar diretório logs se não existir
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    # Criar arquivo .htaccess para Apache
    htaccess_content = """
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /index.py/$1 [QSA,L]

# Configurações de segurança
<Files "db.sqlite3">
    Order allow,deny
    Deny from all
</Files>

<Files "*.py">
    Order allow,deny
    Deny from all
</Files>

# Permitir apenas arquivos estáticos
<FilesMatch "\\.(css|js|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$">
    Order allow,deny
    Allow from all
</FilesMatch>
"""
    
    with open(".htaccess", "w", encoding="utf-8") as f:
        f.write(htaccess_content)
    
    print("✅ Arquivos de produção criados!")

def collect_static():
    """Coleta arquivos estáticos"""
    return run_command(
        "python manage.py collectstatic --noinput",
        "Coletando arquivos estáticos"
    )

def make_migrations():
    """Executa migrações"""
    return run_command(
        "python manage.py makemigrations",
        "Criando migrações"
    )

def migrate():
    """Aplica migrações"""
    return run_command(
        "python manage.py migrate",
        "Aplicando migrações"
    )

def create_superuser():
    """Cria superusuário se não existir"""
    print("\n👤 Verificando superusuário...")
    
    # Verificar se já existe superusuário
    try:
        result = subprocess.run(
            "python manage.py shell -c \"from django.contrib.auth.models import User; print('Superusuário existe' if User.objects.filter(is_superuser=True).exists() else 'Não existe')\"",
            shell=True, capture_output=True, text=True
        )
        
        if "Não existe" in result.stdout:
            print("⚠️  Não foi encontrado superusuário.")
            print("📝 Para criar um superusuário, execute:")
            print("   python manage.py createsuperuser")
        else:
            print("✅ Superusuário já existe!")
            
    except Exception as e:
        print(f"⚠️  Erro ao verificar superusuário: {e}")

def main():
    """Função principal do deploy"""
    print("🚀 INICIANDO DEPLOY DO SISTEMA JAM")
    print("=" * 50)
    
    # Verificar se estamos no diretório correto
    if not Path("manage.py").exists():
        print("❌ Erro: execute este script no diretório raiz do projeto (onde está manage.py)")
        sys.exit(1)
    
    # Passos do deploy
    steps = [
        ("Criando arquivos de produção", create_production_files),
        ("Coletando arquivos estáticos", collect_static),
        ("Criando migrações", make_migrations),
        ("Aplicando migrações", migrate),
    ]
    
    # Executar passos
    for step_name, step_func in steps:
        if not step_func():
            print(f"\n❌ Deploy falhou em: {step_name}")
            sys.exit(1)
    
    # Verificar superusuário
    create_superuser()
    
    print("\n" + "=" * 50)
    print("🎉 DEPLOY CONCLUÍDO COM SUCESSO!")
    print("\n📋 PRÓXIMOS PASSOS:")
    print("1. Faça upload dos arquivos para o servidor FTP")
    print("2. Configure o servidor web (Apache/Nginx)")
    print("3. Crie um superusuário se necessário:")
    print("   python manage.py createsuperuser")
    print("4. Acesse o sistema em: https://sistemajam.com.br")
    print("\n🔧 CONFIGURAÇÕES DO SERVIDOR:")
    print("   - Host: ftp.sistemajam.com.br")
    print("   - Usuário: sistemajam")
    print("   - Senha: SistemaJam2024!")
    print("   - Diretório: /public_html/")

if __name__ == "__main__":
    main() 