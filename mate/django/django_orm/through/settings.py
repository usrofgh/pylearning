from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'django-insecure-_@qagdxbk0g8)l=4c5x8bj%u^za-gt)104v*j8jwbptyvpi5&y'

INSTALLED_APPS = [
    'db'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

USE_TZ = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
