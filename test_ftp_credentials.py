#!/usr/bin/env python3
"""
Script para testar credenciais FTP
"""

import ftplib
import socket

def test_ftp_connection(host, user, password, port=21):
    """Testa conexão FTP com credenciais específicas"""
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, port, timeout=10)
        ftp.login(user, password)
        
        # Se chegou até aqui, a conexão foi bem-sucedida
        print(f"   ✅ SUCESSO! Host: {host}:{port}, User: {user}")
        
        # Listar diretório atual
        print("   📁 Conteúdo do diretório atual:")
        ftp.retrlines('LIST')
        
        ftp.quit()
        return True
        
    except ftplib.error_perm as e:
        print(f"   ❌ Erro de autenticação: {e}")
        return False
    except socket.timeout:
        print(f"   ⏰ Timeout na conexão")
        return False
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def main():
    """Função principal"""
    print("🔍 TESTE DE CREDENCIAIS FTP - SISTEMA JAM")
    print("=" * 50)
    
    # Configurações para testar
    test_configs = [
        # Configurações principais
        ('ftp.sistemajam.com.br', 'sistemajam', 'SistemaJam2024!', 21),
        ('sistemajam.com.br', 'sistemajam', 'SistemaJam2024!', 21),
        ('ftp.sistemajam.com.br', 'sistemajam', 'SistemaJam2024!', 22),
        
        # Variações de usuário
        ('ftp.sistemajam.com.br', 'admin', 'SistemaJam2024!', 21),
        ('ftp.sistemajam.com.br', 'root', 'SistemaJam2024!', 21),
        ('ftp.sistemajam.com.br', 'ftp', 'SistemaJam2024!', 21),
        
        # Variações de senha
        ('ftp.sistemajam.com.br', 'sistemajam', 'sistemajam', 21),
        ('ftp.sistemajam.com.br', 'sistemajam', 'admin', 21),
        ('ftp.sistemajam.com.br', 'sistemajam', '123456', 21),
        ('ftp.sistemajam.com.br', 'sistemajam', 'password', 21),
        
        # Sem senha
        ('ftp.sistemajam.com.br', 'sistemajam', '', 21),
        ('ftp.sistemajam.com.br', 'anonymous', '', 21),
    ]
    
    success_count = 0
    
    for i, (host, user, password, port) in enumerate(test_configs, 1):
        print(f"\n🔌 Teste {i}: {host}:{port}")
        print(f"   Usuário: {user}")
        print(f"   Senha: {'*' * len(password) if password else '(vazia)'}")
        
        if test_ftp_connection(host, user, password, port):
            success_count += 1
            print(f"   🎉 CREDENCIAIS ENCONTRADAS!")
            print(f"   📋 Use estas configurações:")
            print(f"      Host: {host}")
            print(f"      Porta: {port}")
            print(f"      Usuário: {user}")
            print(f"      Senha: {password}")
            break
    
    print(f"\n📊 RESUMO:")
    print(f"   Testes realizados: {len(test_configs)}")
    print(f"   Sucessos: {success_count}")
    
    if success_count == 0:
        print("\n❌ Nenhuma credencial funcionou!")
        print("\n🔧 RECOMENDAÇÕES:")
        print("1. Verifique se as credenciais estão corretas")
        print("2. Confirme com o provedor de hospedagem")
        print("3. Verifique se o FTP está habilitado")
        print("4. Teste via cliente FTP (FileZilla, WinSCP)")

if __name__ == "__main__":
    main() 