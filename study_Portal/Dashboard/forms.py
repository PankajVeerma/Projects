from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
class NotesForm(forms.ModelForm):
  class Meta:
    model = Notes
    fields = ['title','description']
class HomeworkForm(forms.ModelForm):
  class Meta:
    model = Homework
    widgets = {
      'due': forms.DateInput(attrs={'type': 'date'})
    }
    fields = ['subject','title','description','due','is_finished']
# Compare this snippet from study_Portal/Dashboard/models.py:    
class DashboardForm(forms.Form):
  text = forms.CharField(max_length=400, label='Enter Your Search:')

class TodoForm(forms.ModelForm):
  class Meta:
    model = Todo
    fields = ['title','is_finished']  
    
class ConversionForm(forms.Form):
  CHOICES = [('length','Length'),('mass','Mass')]
  measurment = forms.ChoiceField(choices = CHOICES,widget=forms.RadioSelect)  
  
class ConversionLenghtForm(forms.Form):
  CHOICES = [('yard','Yard'),('foot','Foot')]
  input = forms.CharField(required=False,label=False,widget=forms.TextInput(attrs={'type':'number','placeholder':'Enter the Number'}))
  measure1  =forms.CharField(label='',widget= forms.Select(choices=CHOICES))
  measure2  =forms.CharField(label='',widget= forms.Select(choices=CHOICES))
class ConversionMassForm(forms.Form):
  CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
  input = forms.CharField(required=False,label=False,widget=forms.TextInput(attrs={'type':'number','placeholder':'Enter the Number'}))
  measure1  =forms.CharField(label='',widget= forms.Select(choices=CHOICES))
  measure2  =forms.CharField(label='',widget= forms.Select(choices=CHOICES))
  
     

class UserRegistrationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','password1','password2']
