from .base import *

DEBUG = env('DEBUG')


ALLOWED_HOSTS = env('SERVERNAMES').split(' ')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
