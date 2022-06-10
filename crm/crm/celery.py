import os

from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task
def test():
    print('Hello World!')


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'crm.celery.test',
        'schedule': timedelta(seconds=5),

    },
}
app.conf.timezone = 'UTC'
