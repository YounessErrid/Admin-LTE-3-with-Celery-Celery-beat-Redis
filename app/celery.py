# app/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Ensures Celery retries connecting to the broker during startup
app.conf.broker_connection_retry_on_startup = True

# Optional: Example periodic task schedule (every minute)
app.conf.beat_schedule = {
    
    'say-hello-every-minute': {
        'task': 'app.tasks.say_hello',
        'schedule': crontab(minute='*/1'),  # Executes every 1 minute
    },
}


