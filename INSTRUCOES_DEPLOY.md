# 🚀 INSTRUÇÕES DE DEPLOY - SISTEMA JAM

## 📋 Pré-requisitos

- Python 3.8+ instalado no servidor
- Acesso FTP ao servidor
- Servidor web (Apache/Nginx) configurado

## 🔧 Configurações do Servidor FTP

```
Host: ftp.sistemajam.com.br
Usuário: sistemajam
Senha: SistemaJam2024!
Diretório: /public_html/
```

## 📁 Estrutura de Arquivos para Upload

Faça upload dos seguintes arquivos e pastas para `/public_html/`:

```
empresa_nova/
├── manage.py
├── requirements.txt
├── wsgi.py
├── .htaccess
├── empresa_nova/
│   ├── __init__.py
│   ├── settings.py
│   ├── settings_production.py
│   ├── urls.py
│   └── wsgi.py
├── backend/
├── dashboard/
├── website/
├── subscriptions/
├── ai_assistant/
├── modern_ui/
├── templates/
├── staticfiles/
├── media/
├── logs/
└── db.sqlite3
```

## 🛠️ Passos para Deploy

### 1. Upload dos Arquivos
- Conecte-se ao FTP
- Faça upload de todos os arquivos para `/public_html/`
- Certifique-se de que as permissões estão corretas (755 para pastas, 644 para arquivos)

### 2. Instalação das Dependências
No servidor, execute:
```bash
cd /public_html/
pip install -r requirements.txt
```

### 3. Configuração do Banco de Dados
```bash
python manage.py migrate
```

### 4. Criação do Superusuário
```bash
python manage.py createsuperuser
```

### 5. Coleta de Arquivos Estáticos
```bash
python manage.py collectstatic --noinput
```

### 6. Configuração do Servidor Web

#### Para Apache (.htaccess já incluído):
O arquivo `.htaccess` já está configurado para:
- Redirecionar todas as requisições para o Django
- Proteger arquivos sensíveis
- Permitir acesso a arquivos estáticos

#### Para Nginx:
```nginx
server {
    listen 80;
    server_name sistemajam.com.br www.sistemajam.com.br;
    
    location /static/ {
        alias /public_html/staticfiles/;
    }
    
    location /media/ {
        alias /public_html/media/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 🔐 Configurações de Segurança

### 1. Proteção de Arquivos
- `db.sqlite3` - Protegido por .htaccess
- Arquivos `.py` - Protegidos por .htaccess
- Logs - Apenas para administradores

### 2. Configurações de Email
- SMTP configurado para `mail.sistemajam.com.br`
- Usuário: `contato@sistemajam.com.br`
- Senha: `SistemaJam2024!`

## 🌐 URLs do Sistema

- **Site Principal**: https://sistemajam.com.br
- **Sistema ERP**: https://sistemajam.com.br/sistema/
- **Admin Django**: https://sistemajam.com.br/admin/

## 📞 Suporte

Em caso de problemas:
1. Verifique os logs em `/public_html/logs/django.log`
2. Confirme as permissões dos arquivos
3. Teste a conectividade do banco de dados
4. Verifique se o Python e as dependências estão instalados

## 🎯 Funcionalidades Disponíveis

✅ **Site de Vendas Moderno**
✅ **Sistema ERP Completo**
✅ **Dashboard Inteligente**
✅ **Comandos de Voz**
✅ **Interface Responsiva**
✅ **Sistema de Usuários**
✅ **Módulos: Clientes, Produtos, Vendas, Financeiro, etc.**

## 🚀 Status do Deploy

Após seguir todos os passos, o sistema estará disponível em:
**https://sistemajam.com.br**

O sistema mais moderno de ERP do mundo estará online! 🎉 