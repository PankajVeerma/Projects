from django.contrib import admin
from django.urls import path
from Todo.views import home,login,logout,signup,add_todo,signout,delete_todo,change_status

urlpatterns = [
path('',home,name = 'home'),
path('signup/',signup, name='signup'),
path('login/',login , name='login'),
path('logout/',signout,name='signout'),
path('add_todo/',add_todo,name='Addtodo'),
path('delete-todo/<int:id>',delete_todo,name='delete_todo'),
path('change-status/<int:id>/<str:status>',change_status,name='change_todo'),
]