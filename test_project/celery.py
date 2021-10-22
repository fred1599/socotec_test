import os
import time

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

app = Celery("test_project")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    time.sleep(1)
