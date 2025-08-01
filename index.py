#!/usr/bin/env python3
"""
Index file for Sistema JAM - Direct Python execution
"""

import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empresa_nova.settings_production')

# Import Django
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# For direct execution
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv) 