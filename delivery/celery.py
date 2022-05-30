import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'delivery.settings')
app = Celery('delivery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
app.conf.broker_url = BASE_REDIS_URL
