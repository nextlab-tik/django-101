from django.shortcuts import render
import requests

# Create your views here.

def selector(request):
    return render(request, "selector.html")

def index(request, city):
    baseurl = "https://query.yahooapis.com/v1/public/yql"
    query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="{}")'
    result = requests.get(baseurl, params={
        "q": query.format(city),
        "format": "json",
    })
    result = result.json()
    result = result["query"]["results"]["channel"]
    temp = result["item"]["condition"]["temp"]
    result["item"]["condition"]["logo"] = weather_status_logo(
        result["item"]["condition"]["text"])
    logo = result["item"]["condition"]["logo"]
    for forecast in result["item"]["forecast"]:
        forecast["logo"] = weather_status_logo(forecast["text"])
        forecast["high"] = (int(forecast["high"]) - 32) * 5 // 9
        forecast["low"] = (int(forecast["low"]) - 32) * 5 // 9
    temp = (int(temp) - 32) * 5 // 9
    location = result["location"]
    return render(request, "index.html", {
        "weather": temp,
        "location": location,
        "logo": logo,
        "result": result,
    })

def weather_status_logo(status):
    WEATHER_LOGOS = {
        "hot": "hot.png",
        "sunny": "sunny.png",
        "mostly sunny": "sunny.png",
        "thunderstorms": "thunderstorms.png",
        "severe thunderstorms": "thunderstorms.png",
        "scattered thunderstorms": "rain_s_cloudy.png",
        "partly cloudy": "partly_cloudy.png",
        "mostly cloudy": "partly_cloudy.png",
        "cloudy": "cloudy.png",
        "showers": "rain_light.png",
        "scattered showers": "rain_light.png",
        "rain": "rain.png",
        "snow": "snow.png",
        "heavy snow": "snow.png",
        "snow flurries": "snow.png",
        "blowing snow": "snow.png",
        "sleet": "sleet.png",
        "windy": "windy.png",
    }
    return "weather/" + WEATHER_LOGOS.get(status.lower(), "cloudy.png")
