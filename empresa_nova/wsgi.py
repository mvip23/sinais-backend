#!/usr/bin/env python3
"""
WSGI config for empresa_nova project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Adicionar o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configurar as configurações do Django para Railway
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empresa_nova.settings_railway')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
