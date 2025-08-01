#!/usr/bin/env python3
"""
Script de Upload FTP para Sistema JAM
"""

import ftplib
import os
from pathlib import Path

# Configurações FTP
FTP_HOST = "ftp.sistemajam.com.br"
FTP_USER = "sistemajam"
FTP_PASS = "SistemaJam2024!"
FTP_DIR = "/public_html/"

def upload_file(ftp, local_path, remote_path):
    """Upload de um arquivo"""
    try:
        with open(local_path, 'rb') as file:
            ftp.storbinary(f'STOR {remote_path}', file)
        print(f"✅ Upload: {local_path} -> {remote_path}")
        return True
    except Exception as e:
        print(f"❌ Erro no upload de {local_path}: {e}")
        return False

def upload_directory(ftp, local_dir, remote_dir):
    """Upload de um diretório recursivamente"""
    try:
        # Criar diretório remoto se não existir
        try:
            ftp.mkd(remote_dir)
            print(f"📁 Criado diretório: {remote_dir}")
        except:
            pass  # Diretório já existe
        
        # Listar arquivos e pastas
        for item in os.listdir(local_dir):
            local_path = os.path.join(local_dir, item)
            remote_path = f"{remote_dir}/{item}"
            
            if os.path.isfile(local_path):
                upload_file(ftp, local_path, remote_path)
            elif os.path.isdir(local_path):
                upload_directory(ftp, local_path, remote_path)
                
    except Exception as e:
        print(f"❌ Erro no upload do diretório {local_dir}: {e}")

def main():
    """Função principal"""
    print("🚀 INICIANDO UPLOAD FTP DO SISTEMA JAM")
    print("=" * 50)
    
    try:
        # Conectar ao FTP
        print(f"🔌 Conectando ao FTP: {FTP_HOST}")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        print("✅ Conectado com sucesso!")
        
        # Mudar para o diretório de destino
        ftp.cwd(FTP_DIR)
        print(f"📁 Diretório de destino: {FTP_DIR}")
        
        # Lista de arquivos e pastas para upload
        items_to_upload = [
            "manage.py",
            "requirements.txt",
            "wsgi.py",
            ".htaccess",
            "empresa_nova/",
            "backend/",
            "dashboard/",
            "website/",
            "subscriptions/",
            "ai_assistant/",
            "modern_ui/",
            "templates/",
            "staticfiles/",
            "media/",
            "logs/",
            "db.sqlite3"
        ]
        
        # Fazer upload de cada item
        for item in items_to_upload:
            if os.path.exists(item):
                if os.path.isfile(item):
                    upload_file(ftp, item, item)
                elif os.path.isdir(item):
                    upload_directory(ftp, item, item)
            else:
                print(f"⚠️  Item não encontrado: {item}")
        
        # Fechar conexão
        ftp.quit()
        print("\n✅ Upload concluído com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro na conexão FTP: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 UPLOAD CONCLUÍDO!")
    print("\n📋 PRÓXIMOS PASSOS:")
    print("1. Acesse o servidor via SSH")
    print("2. Execute: pip install -r requirements.txt")
    print("3. Execute: python manage.py migrate")
    print("4. Execute: python manage.py createsuperuser")
    print("5. Acesse: https://sistemajam.com.br")
    
    return True

if __name__ == "__main__":
    main() 