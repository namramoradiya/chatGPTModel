import os
from django.core.wsgi import get_wsgi_application

# Replace 'chatapp' with your Django project name if different
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

application = get_wsgi_application()
