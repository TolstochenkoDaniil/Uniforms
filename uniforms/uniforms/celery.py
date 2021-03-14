import os
from celery import Celery

from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uniforms.settings')

celery = Celery('uniforms')
celery.config_from_object(settings, namespace='CELERY')

celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)