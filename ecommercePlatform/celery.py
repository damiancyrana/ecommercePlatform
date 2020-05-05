import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommercePlatform.settings')

app = Celery('ecommercePlatform')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
