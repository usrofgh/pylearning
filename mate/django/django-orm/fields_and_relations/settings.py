from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
INSTALLED_APPS = ["db"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
USE_TZ = False  # при datetime могут быть проблемы
TIME_ZONE = "Europe/Kiev"
USE_T18N = True
LANGUAGE_CODE = "en-us"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
