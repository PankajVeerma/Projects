from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from django import SignUpForm,loginForm
from django.contrib.auth import authenticate  

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
  return render(request,'home.html')  
def signup(request):
    msg='WelCome To This Dashboard'
    if request.method == 'POST':
        form=SignUPForm(request.POST)
        if form.is_vailed():
            user= form.save()
            msge = 'Thank You "\YOu Information is recorded\"'
            return redirect('login')
        else:
            msge = 'Form is Not Vailed'
    else:
        form = SignUpForm()        
        return render(request,'signup.html',{'form':form,'msge':msge})

    pass
def login(request):
    form = loginForm(request.POST or None)
    msg=None
    if form.methode=='POST':
        if form_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username,email=email,password=password)
            if user is not None:
               login(request,user)
               return redirect(home)
            else:
               msg="Invailed Credentials"
        else:
            msg="Error Validation"  
    return redirect(request,'login.html',{'form':form,'msg':msg})             
          
    
