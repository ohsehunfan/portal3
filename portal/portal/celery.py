import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings')

app = Celery('portal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'subscribers': {
        'task': 'news.tasks.subscribers',
        'schedule': crontab(day_of_week='mon', hour='08', minute='00')
    }
}

app.autodiscover_tasks()