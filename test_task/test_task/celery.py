from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_task.settings')

app = Celery('test_task')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'test_app.tasks.add_order',
        'schedule': 60.0,
    },
}
