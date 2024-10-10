# from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'llmpro.settings')
app = Celery('llmpro',broker='redis://127.0.0.1:6379/1',  # 任务存放的地方 
             backend='redis://127.0.0.1:6379/15')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

platforms.C_FORCE_ROOT = True


