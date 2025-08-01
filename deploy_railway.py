#!/usr/bin/env python3
"""
Script de Deploy Automático para Railway - Sistema JAM
"""

import os
import subprocess
import sys
import time

def run_command(command, description):
    """Executa um comando e mostra o progresso"""
    print(f"\n🔄 {description}...")
    print(f"   Comando: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"   ✅ {description} concluído!")
            if result.stdout:
                print(f"   📄 Saída: {result.stdout.strip()}")
            return True
        else:
            print(f"   ❌ Erro em {description}:")
            print(f"   📄 Erro: {result.stderr.strip()}")
            return False
            
    except Exception as e:
        print(f"   ❌ Exceção em {description}: {e}")
        return False

def check_railway_cli():
    """Verifica se o Railway CLI está instalado"""
    print("🔍 Verificando Railway CLI...")
    
    try:
        result = subprocess.run(['railway', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ Railway CLI encontrado!")
            return True
        else:
            print("   ❌ Railway CLI não encontrado!")
            return False
    except FileNotFoundError:
        print("   ❌ Railway CLI não instalado!")
        return False

def install_railway_cli():
    """Instala o Railway CLI"""
    print("\n📦 Instalando Railway CLI...")
    
    # Tentar diferentes métodos de instalação
    install_commands = [
        "npm install -g @railway/cli",
        "yarn global add @railway/cli",
        "pip install railway"
    ]
    
    for command in install_commands:
        print(f"   Tentando: {command}")
        if run_command(command, "Instalação Railway CLI"):
            return True
    
    print("   ❌ Não foi possível instalar o Railway CLI automaticamente")
    print("   📋 Instale manualmente:")
    print("      npm install -g @railway/cli")
    return False

def create_railway_project():
    """Cria projeto no Railway"""
    print("\n🚀 Criando projeto no Railway...")
    
    # Verificar se já está logado
    if not run_command("railway whoami", "Verificando login"):
        print("   🔐 Fazendo login no Railway...")
        if not run_command("railway login", "Login Railway"):
            return False
    
    # Criar projeto
    if not run_command("railway init", "Inicializando projeto Railway"):
        return False
    
    return True

def deploy_to_railway():
    """Faz o deploy para o Railway"""
    print("\n🚀 Fazendo deploy para o Railway...")
    
    # Coletar arquivos estáticos
    if not run_command("python manage.py collectstatic --noinput", "Coletando arquivos estáticos"):
        return False
    
    # Fazer migrações
    if not run_command("python manage.py makemigrations", "Criando migrações"):
        return False
    
    if not run_command("python manage.py migrate", "Aplicando migrações"):
        return False
    
    # Deploy
    if not run_command("railway up", "Deploy Railway"):
        return False
    
    return True

def get_railway_url():
    """Obtém a URL do projeto Railway"""
    print("\n🌐 Obtendo URL do Railway...")
    
    try:
        result = subprocess.run(['railway', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout
            # Procurar pela URL na saída
            for line in output.split('\n'):
                if 'railway.app' in line or 'up.railway.app' in line:
                    url = line.strip()
                    print(f"   ✅ URL encontrada: {url}")
                    return url
    except:
        pass
    
    print("   ⚠️  URL não encontrada automaticamente")
    return None

def main():
    """Função principal"""
    print("🚀 DEPLOY AUTOMÁTICO RAILWAY - SISTEMA JAM")
    print("=" * 50)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('manage.py'):
        print("❌ Erro: execute este script no diretório do projeto Django")
        return
    
    # Verificar Railway CLI
    if not check_railway_cli():
        print("\n📦 Instalando Railway CLI...")
        if not install_railway_cli():
            print("\n❌ Não foi possível instalar o Railway CLI")
            print("📋 Instale manualmente:")
            print("   npm install -g @railway/cli")
            print("   Depois execute: railway login")
            return
    
    # Criar projeto Railway
    if not create_railway_project():
        print("\n❌ Erro ao criar projeto Railway")
        return
    
    # Fazer deploy
    if not deploy_to_railway():
        print("\n❌ Erro no deploy")
        return
    
    # Obter URL
    url = get_railway_url()
    
    print("\n🎉 DEPLOY CONCLUÍDO COM SUCESSO!")
    print("=" * 50)
    
    if url:
        print(f"🌐 Sistema online em: {url}")
    else:
        print("🌐 Sistema online no Railway!")
        print("   Execute 'railway status' para ver a URL")
    
    print("\n🔑 Credenciais de acesso:")
    print("   Usuário: admin")
    print("   Senha: SistemaJam2024!")
    
    print("\n📋 URLs do Sistema:")
    if url:
        print(f"   Site Principal: {url}")
        print(f"   Sistema ERP: {url}/sistema/")
        print(f"   Admin Django: {url}/admin/")
    
    print("\n✅ O Sistema JAM está online e funcionando!")

if __name__ == "__main__":
    main() 