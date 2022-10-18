from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hotel_booking_system.settings')

app = Celery('Hotel_bokking_system')
app.conf.enable_utc = False
app.conf.update(timezone = 'Africa/Lagos')
app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTINGS

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')
