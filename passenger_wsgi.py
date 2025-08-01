#!/usr/bin/env python3
"""
Passenger WSGI configuration for Sistema JAM
"""

import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empresa_nova.settings_production')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 