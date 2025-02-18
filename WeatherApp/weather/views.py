from django.shortcuts import render
import datetime
import requests
from math import *

# Create your views here.
def index(request):
  try:
      
    if request.method =='GET':
      data={}
      city= 'New Delhi'
      city = str(request.GET.get('search','Delhi'))
      api_key = "Enter your own APi Key"
      base_url = "https://api.openweathermap.org/data/2.5/weather?q="
  
      complete_Url= base_url + city  + "&appid="  + api_key
      response =requests.get(complete_Url)
      data_formate  = response.json()
      kelvin = data_formate["main"]["temp"]
      Celsius = round(kelvin - 273.15 ) 
      wind_speed = data_formate["wind"]["speed"]
      wind_speed =ceil((wind_speed)*(18//5))
      humidity = data_formate["main"]["humidity"]
      vist = data_formate["visibility"]
      clouds=data_formate["clouds"]["all"]
      dist = data_formate["weather"][0]["description"]
      
      data = {
        'city':city,
        'Celsius':Celsius,
        'humidity':humidity,
        'vist':vist,
        'dist':dist,
        "cloud":clouds,
        "wind_Speed":wind_speed
        }
      return render(request,'index.html',data)
  except EOFError:
      return render(request,'index.html')