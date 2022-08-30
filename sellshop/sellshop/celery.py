from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sellshop.settings')
app = Celery('sellshop')
from django.apps import apps 

app.config_from_object(settings)
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):   
    print('Request: {0!r}'.format(self.request))

# code for run celery:
#celery -A sellsh worker --beat -S django -l info
# for development
#celery -A sellshop worker --beat --scheduler django --loglevel=info