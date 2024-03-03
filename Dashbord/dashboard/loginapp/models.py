from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_admine=models.BooleanField('Is Admin',default=False)
    is_docter=models.BooleanField('Is Docter',default=False)
    is_patient=models.BooleanField('Is Patient',default=False)
