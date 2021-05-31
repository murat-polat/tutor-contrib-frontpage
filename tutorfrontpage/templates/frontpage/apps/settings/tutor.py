from .common import *
from .settings import *

SECRET_KEY = "{{ FRONTPAGE_SECRET_KEY }}"
ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "mysql",
        "PORT": 3306,
        "NAME": "frontpage",
        "USER": "frontpage",
        "PASSWORD": "frontpage",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}