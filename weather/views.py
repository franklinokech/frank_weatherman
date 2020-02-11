# Import requests package
import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=03275f93eb34f52008163cf91cac0841'
    city = 'Mombasa'

    # Convert the request to json format to be used in the getting the data
    r = requests.get(url.format(city)).json()

    # Store the response in a dictionary
    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    # For testing purposes, uncomment
    # print(city_weather)

    # Store the dictionary in a context variable to be sent to the template
    context = {'city_weather': city_weather}

    # Send the context dictionary with the render function to get the html page
    return render(request, 'weather/weather.html', context)
