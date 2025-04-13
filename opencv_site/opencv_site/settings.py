
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'demo-secret-key'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'imageapp',
]

MIDDLEWARE = []

ROOT_URLCONF = 'opencv_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]

WSGI_APPLICATION = 'opencv_site.wsgi.application'

MEDIA_URL = '/'
MEDIA_ROOT = os.path.join(BASE_DIR, '')

STATIC_URL = '/static/'
