
import requests 
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9d6afce7f9df4043397abe33fbf8a6ca'
    city = 'Las Vegas'

    r = requests.get(url.format(city))
    print(r.text)

    return render(request, 'weather/weather.html')