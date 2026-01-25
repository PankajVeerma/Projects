# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings  
# from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerydemo.settings')
# app = Celery('celerydemo')
# app.conf.enable_utc = False
# app.conf.update(timezone='Asia/Kolkata')
# app.config_from_object(settings, namespace='CELERY')

# celery beat 
# app.conf.beat_schedule = {
#     "sending_mail_every_hour":{
#         "task": "celeryapp.tasks.sending_email_task",
#         # "schedule": crontab(hour=22, minute=16),  # every 1 minute
#         "schedule": crontab(minute='*/1'),  # every 1 minute
#     }}



# for par Particular time email sending schedule task    for send_mail_to_user_to_the_Particular_Time
# app.conf.beat_schedule = {
#     "sending_mail_every_hour":{
#         "task": "celeryapp.tasks.sending_email_task_periodic",
        # "schedule": crontab(hour=22, minute=16),  # every 1 minute
        # "schedule": crontab(minute='*/1'),  # every 1 minute
        # "schedule": crontab(hour=0, minute=45, day_of_week='mon-sun'), # everyday at 12:45 AM
        # "schedule": crontab(hour=0, minute=5),  # everyday at 12:45 AM
        # "schedule": crontab(hour=0, minute=45, day_of_month=31)  # everyday at 12:45 AM
#     }}

# # app.autodiscover_tasks()
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab  # you need to import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerydemo.settings')

app = Celery('celerydemo')

app.config_from_object(settings, namespace='CELERY')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

# Static beat schedule for sending emails at 12:05 AM
app.conf.beat_schedule = {
    "send_daily_email_12_05_am": {
        "task": "celeryapp.tasks.sending_email_task_periodic",  # must match task name
        "schedule": crontab(hour=0, minute=47),  # 12:05 AM every day
        "args": (),  # no arguments
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
