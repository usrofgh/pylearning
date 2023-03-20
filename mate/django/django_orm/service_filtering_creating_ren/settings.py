from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'django-insecure-7zy+mxx5oo)6^-0=x-f8judd(-x=ss9%720nd5x(%!a-e__e19'

INSTALLED_APPS = [
    'db',
    'django_extensions'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

USE_TZ = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
