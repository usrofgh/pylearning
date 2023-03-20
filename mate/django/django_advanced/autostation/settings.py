from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'django-insecure-2+0$y*@kr484g(0$e3y0_w6$p366j@s^l#pnjoel-*v5n^p%rw'

INSTALLED_APPS = [
    'db',
    'django_extensions',
    'django.contrib.auth',
    'django.contrib.contenttypes'
]

AUTH_USER_MODEL = "db.User"

AUTH_PASSWORD_VALIDATORS = [  # for creating good passwords, not weak
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

USE_TZ = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
