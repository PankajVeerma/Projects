from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('note',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_notes,name="delete_notes"),
    path('note_detail/<int:pk>',views.NotesDetailView.as_view(),name="note_detail"),
    path('homework',views.homework,name="homework"),
    path('update_homework/<int:pk>',views.update_homework,name="update_homework"),
    path('dalete_homework/<int:pk>',views.dalete_homework,name="dalete_homework"),
    path('youtube',views.youTube,name="youtube"),
    path('todo',views.Todo_list,name="todo"),
    path('update_todo/<int:pk>',views.update_todo,name="update_todo"),
    path('dalete_todo/<int:pk>',views.dalete_todo,name="dalete_todo"),
    path('books',views.books,name="books"),
    path('dictionary',views.dictionary,name="dictionary"),
    path('wikipedia',views.wikipedia,name="wikipedia"),
    path('conversion',views.conversion,name="conversion"),
   
   
]
