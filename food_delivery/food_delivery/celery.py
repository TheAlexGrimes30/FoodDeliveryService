import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery.settings')

app = Celery('food_delivery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
