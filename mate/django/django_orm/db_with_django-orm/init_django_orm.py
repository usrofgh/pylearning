import sys
import os
import django


sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()
