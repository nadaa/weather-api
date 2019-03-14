from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=a69cf62636f4987574f1cbbc3af4cc43'
    r = requests.get(url).json()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    data_weather = []

    for city in cities:

        city_weather = {
            'city': city.name,
            'tempreture':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        data_weather.append(city_weather)

    context = {'weather_data':data_weather, 'form':form}
    return render(request, 'weather/weather.html',context)