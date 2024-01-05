from .base import *


SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = ['localhost']

LOCAL_APPS = [
    "core.weather",
]

INSTALLED_APPS += LOCAL_APPS




