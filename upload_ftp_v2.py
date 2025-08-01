#!/usr/bin/env python3
"""
Script de Upload FTP Robusto para Sistema JAM
"""

import ftplib
import os
import time
from pathlib import Path

def upload_file(ftp, local_path, remote_path):
    """Upload de um arquivo"""
    try:
        with open(local_path, 'rb') as file:
            ftp.storbinary(f'STOR {remote_path}', file)
        print(f"   ✅ {local_path} -> {remote_path}")
        return True
    except Exception as e:
        print(f"   ❌ Erro ao fazer upload de {local_path}: {e}")
        return False

def create_remote_dir(ftp, remote_dir):
    """Cria diretório remoto se não existir"""
    try:
        ftp.mkd(remote_dir)
        print(f"   📁 Diretório criado: {remote_dir}")
    except ftplib.error_perm as e:
        if "550" in str(e):  # Diretório já existe
            pass
        else:
            print(f"   ⚠️  Erro ao criar diretório {remote_dir}: {e}")

def upload_directory(ftp, local_dir, remote_dir=""):
    """Upload recursivo de diretório"""
    success_count = 0
    total_count = 0
    
    for root, dirs, files in os.walk(local_dir):
        # Calcular caminho remoto
        rel_path = os.path.relpath(root, local_dir)
        if rel_path == '.':
            current_remote_dir = remote_dir
        else:
            current_remote_dir = os.path.join(remote_dir, rel_path).replace('\\', '/')
        
        # Criar diretório remoto
        if current_remote_dir:
            create_remote_dir(ftp, current_remote_dir)
        
        # Upload de arquivos
        for file in files:
            local_file = os.path.join(root, file)
            remote_file = os.path.join(current_remote_dir, file).replace('\\', '/')
            
            total_count += 1
            if upload_file(ftp, local_file, remote_file):
                success_count += 1
            
            # Pequena pausa para não sobrecarregar
            time.sleep(0.1)
    
    return success_count, total_count

def main():
    """Função principal"""
    print("🚀 UPLOAD FTP ROBUSTO - SISTEMA JAM")
    print("=" * 50)
    
    # Configurações FTP
    ftp_configs = [
        {
            'host': 'ftp.sistemajam.com.br',
            'user': 'sistemajam',
            'pass': 'SistemaJam2024!',
            'port': 21
        },
        {
            'host': 'sistemajam.com.br',
            'user': 'sistemajam',
            'pass': 'SistemaJam2024!',
            'port': 21
        },
        {
            'host': 'ftp.sistemajam.com.br',
            'user': 'sistemajam',
            'pass': 'SistemaJam2024!',
            'port': 22
        }
    ]
    
    ftp = None
    connected = False
    
    # Tentar diferentes configurações
    for i, config in enumerate(ftp_configs, 1):
        print(f"\n🔌 Tentativa {i}: Conectando ao FTP...")
        print(f"   Host: {config['host']}:{config['port']}")
        print(f"   Usuário: {config['user']}")
        
        try:
            ftp = ftplib.FTP()
            ftp.connect(config['host'], config['port'], timeout=30)
            ftp.login(config['user'], config['pass'])
            
            print("   ✅ Conexão FTP estabelecida!")
            connected = True
            break
            
        except Exception as e:
            print(f"   ❌ Falha na tentativa {i}: {e}")
            if ftp:
                try:
                    ftp.quit()
                except:
                    pass
    
    if not connected:
        print("\n❌ Não foi possível conectar ao FTP!")
        print("\n📋 VERIFICAÇÕES NECESSÁRIAS:")
        print("1. Confirme as credenciais FTP")
        print("2. Verifique se o servidor está online")
        print("3. Teste a conectividade: ping ftp.sistemajam.com.br")
        print("4. Verifique se a porta 21 está aberta")
        print("\n🔧 ALTERNATIVA:")
        print("Use um cliente FTP como FileZilla ou WinSCP")
        print("Host: ftp.sistemajam.com.br")
        print("Usuário: sistemajam")
        print("Senha: SistemaJam2024!")
        return
    
    try:
        # Listar diretório atual
        print("\n📁 Diretório atual no servidor:")
        ftp.retrlines('LIST')
        
        # Verificar se existe public_html
        try:
            ftp.cwd('public_html')
            print("   ✅ Diretório public_html encontrado")
        except:
            print("   ⚠️  Diretório public_html não encontrado, criando...")
            ftp.mkd('public_html')
            ftp.cwd('public_html')
        
        # Upload dos arquivos
        print("\n📤 Iniciando upload dos arquivos...")
        
        # Lista de arquivos e diretórios para upload
        upload_items = [
            'manage.py',
            'requirements.txt',
            'wsgi.py',
            'passenger_wsgi.py',
            'index.py',
            '.htaccess',
            'empresa_nova/',
            'backend/',
            'dashboard/',
            'website/',
            'subscriptions/',
            'ai_assistant/',
            'modern_ui/',
            'templates/',
            'staticfiles/',
            'media/',
            'logs/',
            'db.sqlite3'
        ]
        
        success_count = 0
        total_count = 0
        
        for item in upload_items:
            if os.path.exists(item):
                if os.path.isfile(item):
                    # Upload de arquivo
                    if upload_file(ftp, item, item):
                        success_count += 1
                    total_count += 1
                else:
                    # Upload de diretório
                    print(f"\n📁 Upload do diretório: {item}")
                    s, t = upload_directory(ftp, item, item)
                    success_count += s
                    total_count += t
            else:
                print(f"   ⚠️  Item não encontrado: {item}")
        
        print(f"\n📊 RESUMO DO UPLOAD:")
        print(f"   ✅ Sucessos: {success_count}")
        print(f"   📁 Total: {total_count}")
        print(f"   📈 Taxa de sucesso: {(success_count/total_count*100):.1f}%")
        
        if success_count > 0:
            print("\n🎉 UPLOAD CONCLUÍDO COM SUCESSO!")
            print("\n🌐 URLs do Sistema:")
            print("   Site Principal: https://sistemajam.com.br")
            print("   Sistema ERP: https://sistemajam.com.br/sistema/")
            print("   Admin: https://sistemajam.com.br/admin/")
            print("\n🔑 Credenciais:")
            print("   Usuário: admin")
            print("   Senha: SistemaJam2024!")
        else:
            print("\n❌ Nenhum arquivo foi enviado com sucesso!")
    
    except Exception as e:
        print(f"\n❌ Erro durante o upload: {e}")
    
    finally:
        if ftp:
            try:
                ftp.quit()
                print("\n🔌 Conexão FTP encerrada")
            except:
                pass

if __name__ == "__main__":
    main() 