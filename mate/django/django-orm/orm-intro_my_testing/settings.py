from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
INSTALLED_APPS = ["db"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
USE_TZ = False
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

