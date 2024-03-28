from django.shortcuts import render
import requests
import datetime
# Create your views here.

def home(request):
    
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f501318988236c2c1f809344fb365f5a'