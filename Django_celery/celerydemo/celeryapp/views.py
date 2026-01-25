from django.shortcuts import HttpResponse
from .tasks import test_func, sending_email_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule

import json
def index(request):
    test_func.delay()
    return HttpResponse("Task submitted")


def send_mail_to_user(request):
    sending_email_task.delay()
    return HttpResponse("Email Send to the all users successfully")
import json
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule

def send_mail_to_user_to_the_particular_time(request, hour=0, minute=30):
    """
    Schedule the 'sending_email_task' to run daily at the given hour and minute.
    Default: 12:00 AM (hour=0, minute=0)
    """
    # Create or get a schedule
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=str(hour),
        minute=str(minute),
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
        timezone='Asia/Kolkata'
    )

    # Unique task name (you can append time for uniqueness)
    task_name = f"send_email_at_{hour}_{minute}"

    # Create the periodic task only if it doesn't exist
    if not PeriodicTask.objects.filter(name=task_name).exists():
        PeriodicTask.objects.create(
            crontab=schedule,
            name=task_name,
            task="celeryapp.tasks.sending_email_task",
            args=json.dumps([]),
            enabled=True
        )
        return HttpResponse(f"Email task scheduled successfully for {hour}:{minute:02d}")
    else:
        return HttpResponse(f"Email task already exists for {hour}:{minute:02d}")
