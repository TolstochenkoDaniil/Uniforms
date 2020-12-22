import os
from celery import Celery

from django.conf import settings

__all__ = [
    'celery'
]

os.environ.setdefault('DJANGO_SETTING_MODULE', 'uniforms.settings')

celery = Celery('uniforms')
celery.config_from_object(settings)

celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)