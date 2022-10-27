import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'get_coins_data_5s':{
        'task': 'coins.tasks.get_coins_data',
        'schedule': 5.0
    }
}

app.autodiscover_tasks()