from django.urls import path  
from ecomerceapp import views
urlpatterns = [
    
   
   
    path('',views.home , name="home"),
   
    path('contact',views.contact , name="contact"),
    path('about',views.about , name="about"),
    path('profile',views.profile , name="profile"),
    path('checkout/',views.checkout , name="Checkout"),
    path('handlerequest/',views.handlerequest , name="handlerequest"),

]