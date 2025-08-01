"""
Django settings for empresa_nova project - PRODUÇÃO
"""

from .settings import *
import os

# Configurações de Produção
DEBUG = False

# Hosts permitidos para produção
ALLOWED_HOSTS = [
    'www.sistemajam.com.br',
    'sistemajam.com.br',
    'localhost',
    '127.0.0.1'
]

# Configurações de Banco de Dados para Produção
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configurações de Email para Produção
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.sistemajam.com.br'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'contato@sistemajam.com.br'
EMAIL_HOST_PASSWORD = 'SistemaJam2024!'
DEFAULT_FROM_EMAIL = 'contato@sistemajam.com.br'

# Configurações de Arquivos Estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Configurações de Mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configurações de Segurança
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Configurações de Sessão
SESSION_COOKIE_SECURE = False  # Mudar para True se usar HTTPS
CSRF_COOKIE_SECURE = False     # Mudar para True se usar HTTPS

# Configurações de Log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Criar diretório de logs se não existir
os.makedirs(BASE_DIR / 'logs', exist_ok=True) 