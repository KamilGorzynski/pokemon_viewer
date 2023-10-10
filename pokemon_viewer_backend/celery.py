import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemon_viewer_backend.settings')

app = Celery('pokemon_viewer_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
