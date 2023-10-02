from django.shortcuts import render
from django.http import HttpResponse


# app_name register, {% url app_name:view %}
app_name = "template_app"

def index(request):
    return render(request, "template_app/first.html")

def weather_view(request):
    weather_dict={
        "istanbul" : "30",
        "batman" : "40",
        "paris" : [10,14,17,13],
        "rome": {"morning":10, "evening":12},
        "user_premium": False,
        "test": "Test test Test test"
        }
    return render(request, 'template_app/weather.html', context=weather_dict)