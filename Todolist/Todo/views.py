from django.shortcuts import render ,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from Todo.forms import TodoForm
from Todo.models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
     if request.user.is_authenticated:
        user = request.user
        form = TodoForm
        todos = Todo.objects.filter(user = user).order_by('priority')
        return render(request,'index.html',context={'form' :form,'todos': todos})
def signup(request):
    if request.method=='GET':
        form = UserCreationForm()
        contex ={
            "form" : form
        }
        return render(request,'signup.html',context=contex)
    else:
        form = UserCreationForm(request.POST)
        contex =   {
            "form" : form
        }
       
        if form.is_valid:
           user = form.save()
       
           if user is not None:
               return redirect('login')
            
        else:
            return render(request,'signup.html',context=contex)
           
def login(request):
    if request.method=="GET":
      form = AuthenticationForm()
      context= {
          "form":form
      }
      return render(request,'login.html' ,context=context)
    else:
        form = AuthenticationForm(data=request.POST)
      
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
            
        else:
            context= {
                "form":form
            }
            return render(request,'login.html' ,context=context)
   
@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
   
        form =TodoForm(request.POST)
        if form.is_valid():
          print(form.cleaned_data)
          todo = form.save(commit=False)
          todo.user = user
          todo.save()
          return redirect("home")
        else:
            form = TodoForm()
            return render(request,'index.html',context ={'form' :form})    
@login_required(login_url='login')       
def signout(request):
    logout(request)
    return redirect('login')
def delete_todo(request,id):
    print(id)
    Todo.objects.get(pk=id).delete()
    return redirect('home')
def change_status(request,id ,status):
    todo = Todo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')