from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'django-insecure-mbve#@w0x#2ls9$708y8+6$=3x)6e0^b3w5j*&_00c@9onwh#w'

INSTALLED_APPS = [
    "db",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
USE_TZ = False
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
