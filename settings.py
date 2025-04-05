import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'your-secret-key'
DEBUG = True
ROOT_URLCONF = 'urls'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = ['django.contrib.staticfiles', 'chatapp']

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'chatapp', 'templates')],
    'APP_DIRS': True,
}]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'chatapp', 'static')]
