from .base import *

DEBUG = env('DEBUG')

STATIC_URL = '/static/static/'
STATIC_ROOT = '/vol/web/static'


ALLOWED_HOSTS = env('SERVERNAMES').split(' ')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
