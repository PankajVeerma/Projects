from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages 
from django.views import generic
from youtubesearchpython import VideosSearch
from . models import *
import requests
import wikipedia




# Create your views here.
def home(request):
  return render(request, './home.html')
def notes(request):
  if request.method == 'POST':
    form = NotesForm(request.POST)
    if form.is_valid():
      notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
      notes.save()
    messages.success(request, 'Notes added successfully')
  else:
      form = NotesForm()
  notes = Notes.objects.filter(user = request.user)
  contex = {
    'notes':notes,
    'form':form,
    
  }
  return render(request, './notes.html',contex)
def delete_notes(request,pk=None):
  notes = Notes.objects.get(id=pk)
  notes.delete()
  messages.success(request, 'Notes deleted successfully')
  return redirect('notes')
class NotesDetailView(generic.DetailView):
  model = Notes

def homework(request):
  if request.method == 'POST':
    form = HomeworkForm(request.POST) 
    if form.is_valid():
      try:
        finished = request.POST['is_finished']
        if finished == 'on':
          finished = True
        else:
          finished = False
      except:
        finished = False
      homework = Homework(
        user=request.user,
        subject=request.POST['subject'],
        title=request.POST['title'],
        description=request.POST['description'],
        due=request.POST['due'],
        is_finished=finished)
      homework.save()
      messages.success(request, 'Homework added successfully')
      
  else:
      form = HomeworkForm()
    
  homework = Homework.objects.filter(user=request.user)
  if len(homework) == 0:
    homework_done = True
    messages.info(request, 'No homework')
  else:
    homework_done = False
    messages.info(request, 'homework Pending')
  context = {
    'homework':homework,
    'homework_done':homework_done,
    'form':form,
  }
  return render(request, './homework.html',context)

def update_homework(request,pk=None):
  homework = Homework.objects.get(id=pk)
  if homework.is_finished  == True:
          homework.is_finished = False
  else:
          homework.is_finished = True
  homework.save()        
  return redirect('homework')


def dalete_homework(request,pk=None):
  homework = Homework.objects.get(id=pk)
  homework.delete()
  messages.success(request, 'Homework deleted successfully')
  return redirect('homework')

# This feature is not working it give errors
def youTube(request):
  if request.method == 'POST':
    form = DashboardForm(request.POST)
    text = request.POST['text']
    video = VideosSearch(text, limit=10)
    result_list = []
    for i in video.result()['result']:
      result_dict = {
        'input':text,
        'duration':i['duration'],
        'publishTime':i['publishedTime'],
        'description':i['description'],
        'title':i['title'],
        'thumbnails':i['thumbnails'][0]['url'],
        'link':i['link'],
        'channel':i['channel']['name'],
        'views':i['viewCount']['short']
        }            
      desc = ''
      if i['descriptionSnippet']:
        for j in i['descriptionSnippet']:
          desc += j['text']
      result_dict['description'] = desc
      result_list.append(result_dict)
      context = {
      'form':form,
      'results':result_list
      } 
      print(result_dict)
      return render(request, './youTube.html',context)
  else:
    form = DashboardForm()
    context = {
          'form':form
  }
  return render(request, './youTube.html',context)


def Todo_list(request):
  todo = Todo.objects.filter(user=request.user)
  if request.method == 'POST':
    form = TodoForm(request.POST) 
    if form.is_valid():
      try:
        finished = request.POST['is_finished']
        if finished == 'on':
          finished = True
        else:
          finished = False
      except:
        finished = False
      todo = Todo(
        user=request.user,
        title=request.POST['title'],
        is_finished=finished)
      todo.save()
      messages.success(request, 'Todo added successfully')
      
  else:
      form = TodoForm()
    
  todo = Todo.objects.filter(user=request.user)
  if len(todo) == 0:
    todo_done = True
    messages.info(request, 'No homework')
  else:
    todo_done = False
    messages.info(request, 'Todo Pending')
  context = {
    'todos':todo,
     'form':form,
     'todo_done':todo_done,
  }
  return render(request, './todo.html',context)


def update_todo(request,pk=None):
  todo = Todo.objects.get(id=pk)
  if todo.is_finished  == True:
          todo.is_finished = False
  else:
          todo.is_finished = True
  todo.save()        
  return redirect('todo')


def dalete_todo(request,pk=None):
  todo = Todo.objects.get(id=pk)
  todo.delete()
  messages.success(request, 'todo deleted successfully')
  return redirect('todo')



def books(request):
  if request.method == 'POST':
    form = DashboardForm(request.POST)
    text = request.POST['text']
    url = 'https://www.googleapis.com/books/v1/volumes?q='+text
    response = requests.get(url)
    data = response.json()
    result_list = []
    for i in range(10):
      result_dict = {
       'title':data['items'][i]['volumeInfo']['title'],
       'description':data['items'][i]['volumeInfo'].get('description'),
       'subtitle':data['items'][i]['volumeInfo'].get('subtile'),
        'authors':data['items'][i]['volumeInfo'].get('authors',),
        'count':data['items'][i]['volumeInfo'].get('pageCount'),
        'categories':data['items'][i]['volumeInfo'].get('categories'),
        'rating':data['items'][i]['volumeInfo'].get('pageRating'),
        'preview':data['items'][i]['volumeInfo'].get('previewLink'),
       
        'thumbnail':data['items'][i]['volumeInfo'].get('imageLinks') 
        },     
      result_list.append(result_dict)
      context = {
      'form':form,
      'results':result_list
      } 
      print(result_dict)
      return render(request,'./books.html',context)
  else:
    form = DashboardForm()
    context = {
          'form':form
  }
  return render(request, './books.html',context)



def dictionary(request):
  if request.method == 'POST':
    form = DashboardForm(request.POST)
    text = request.POST['text']
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+text
    response = requests.get(url)
    data = response.json()
    try:
      phonetics = data[0]['phonetics'][0]['text']
      audio = data[0]['phonetics'][0]['audio']
      definition = data[0]['meanings'][0]['definitions'][0]['definition']
      example = data[0]['meanings'][0]['definitions'][0]['example']
      synonyms = data[0]['meanings'][0]['definitions'][0]['synonyms']
      context = {
        'form':form,
        'input':text,
        'phonetics':phonetics,
        'audio':audio,
        'definition':definition,
        'example':example,
        'synonyms':synonyms,
       }
      
    except:
       context = {
        'form':form,
        'input':text
       }
    print(context['synonyms'])
    return render(request,'./dictonary.html',context)
  else:
    
      form = DashboardForm()  
      context = {'form':form}     
  return render(request,'./dictonary.html',context)


def wikipedia(request):
  if request.method == 'POST':
    text = request.POST['text']
    form = DashboardForm(request.POST)
    search = wikipedia.page("india")
    context = {
      'form':form,
      'title':search.title,
      'link':search.url,
      'details':search.summary
    }
    return render(request,'./wikipedia.html',context)
  else:
    form = DashboardForm()
    context={
      'form':form
      }
  return render(request,'./wikipedia.html',context)
def conversion(request):
  if request.method=='POST':
    form = ConversionForm(request.POST)
    if request.POST['measurment'] == 'length':
      measurement_form = ConversionLenghtForm()
      context  ={
        'form':form,
          'm_form':measurement_form,
          'input':True
           }
      if 'input' in request.POST:
          first = request.POST['measure1'] 
          second = request.POST['measure2'] 
          input= request.POST['input']
          answer = ''
          if input and int(input)>=0:
            if first =='yard' and second =='foot':
              answer = f'{input} Yard = {int(input)*3}'
          
            if first =='foot' and second =='yard':
              answer = f'{input} foot = {int(input)/3}'
          context = {
            'form':form,
            'm_form':measurement_form,
            'input':True,
            'answer':answer
          }    
    if request.POST['measurment']=='mass':
      measurement_form = ConversionMassForm()
      context  ={
        'form':form,
          'm_form':measurement_form,
          'input':True
           }
      if 'input' in request.POST:
          first = request.POST['measure1'] 
          second = request.POST['measure2'] 
          input= request.POST['input']
          answer = ''
          if input and int(input)>=0:
            if first =='pound' and second =='kilogram':
              answer = f'{input} pound = {int(input)*0.453592} kilogram'
          
            if first =='kilogram' and second =='pound':
              answer = f'{input} kilogram = {int(input)*2.20462} pound'
          context = {
            'form':form,
            'm_form':measurement_form,
            'input':True,
            'answer':answer
          }    
          
    else:
        pass
  else:  
    form = ConversionForm()
    context  ={
  'form':form,
  'input':False
    }
  return render(request,'./conversion.html',context)


def register(request):
  if request.method =='POST':
    form = UserRegistrationForm()
    if form.is_valid():
      username = form.cleaned_data.get('username')
      messages.success(request,f"Account Created")
      # return redirect('login')
  else:
    form = UserRegistrationForm() 
  context = {
    'form':form
  }
  return render(request,"./register.html",context)


def profile(request):
  homeworks = Homework.objects.filter(is_finished=False, user=request.user)   
  todos = Todo.objects.filter(is_finished = False, user=request.user)   
  if len(homeworks) ==0:
    homework_done = True
  else:
    homework_done = False
  if len(todos) ==0:
    todo_done = True
  else:
    todo_done = False
  contex= {
    'homeworks':homeworks,
    'todos':todos,
    'homework_done':homework_done,
    'todo_done':todo_done
  }        
  return render(request,'profile.html',contex) 