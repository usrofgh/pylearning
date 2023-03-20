from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'django-insecure-#c6t@-rd*r*a9=@(r&x8p9=y_j#gse-j$(6nh0iy!tvdz6-cb*'

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
