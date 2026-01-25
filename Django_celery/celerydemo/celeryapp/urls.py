from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send_mail_to_user, name='index-send'),
    path('send-particular-mail/', views.send_mail_to_user_to_the_particular_time, name='index-send-particular'),
]
