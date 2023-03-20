from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'django-insecure-=*28%x$r14t^i4@!4%ngf9ot0!dg%*4j8ftp(tu^&@25wuhp1l'

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
