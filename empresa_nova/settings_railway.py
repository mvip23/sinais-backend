"""
Configurações do Django para Railway
"""

import os
import dj_database_url
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Temporariamente True para ver erros

# Configuração da chave secreta
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-^8cg*47v9qe5ye9miybl@qf=xp$z&p_m*g^yb4h0te54b%p@$o')

# Configuração do Railway - Permitir todos os hosts
ALLOWED_HOSTS = ['*']

# Configuração do banco de dados PostgreSQL do Railway
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # Fallback para SQLite se não houver DATABASE_URL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Configuração de arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Configuração de mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuração de segurança - Desabilitar temporariamente
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = None
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Configuração de logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Mudado para DEBUG
    },
}

# Configuração de email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configuração de CORS - Permitir tudo temporariamente
CORS_ALLOWED_ORIGINS = ['*']
CORS_ALLOW_ALL_ORIGINS = True

# Configuração de CSRF - Permitir tudo temporariamente
CSRF_TRUSTED_ORIGINS = ['*']

# Configuração de sessão
SESSION_COOKIE_AGE = 86400  # 24 horas
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Configuração de cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Configuração de middleware para produção
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para arquivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração do WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 