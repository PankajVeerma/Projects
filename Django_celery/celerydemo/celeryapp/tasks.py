from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
  
@shared_task(bind=True)
def test_func(self):
  for i in range(10):
    print("processing...",i)
  return "Done"




@shared_task(bind=True)
def sending_email_task(self):
    user=get_user_model().objects.all()
    for u in user:
      mail_subject = "Hi  Celery Testing"
      mail_message = "Some thing new life  we have to learn and explore"
      to_email = u.email
      send_mail(
        subject=mail_subject,
        message=mail_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
        fail_silently=True,
      )
      print("EMAIL TASK EXECUTED")
    return "Email sent successfully"



# for schedular task with particular time email sending
@shared_task(bind=True)
def sending_email_task_periodic(self,a,b):
    user=get_user_model().objects.all()
    for u in user:
      mail_subject = "Hi  Celery Testing"
      mail_message = "Some thing new life  we have to learn and explore"
      to_email = u.email
      send_mail(
        subject=mail_subject,
        message=mail_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
        fail_silently=True,
      )
      print("EMAIL TASK EXECUTED")
    return "Email sent successfully"