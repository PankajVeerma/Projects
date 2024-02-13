"""
URL configuration for Office_Emp_Manage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('Add_Employee', views.Add_Employee,name='Add_Employee'),
    path('Remove_Employee', views.Remove_Employee,name='Remove_Employee'),
    path('Remove_Employee/<int:emp_id>', views.Remove_Employee,name='Remove_Employee'),
    path('All_Employee', views.All_Employee,name='All-Employee'),
    path('Filter_Employee', views.Filter_Employee,name='Filter_Employee'),
]
