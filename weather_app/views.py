import requests

from rest_framework import viewsets

from weather_app.models import Weather
from weather_app.serializers import WeatherSerializer


class WeatherAppViewSet(viewsets.ModelViewSet):
    serializer_class = WeatherSerializer

    def get_queryset(self):
        data = Weather.objects.all()
        print(data)
        return data

    def _get_weather_data(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=<City>&appid=<API-KEY>"
        response = requests.get(url)
        print(response.json())

        try:
            response.raise_for_status()
            return response.json()
        except:
            return None

    def save_weather_data(self):
        weather_data = self._get_weather_data()
        print(weather_data)
        if weather_data is not None:
            try:
                weather_obj = Weather.objects.create(temperature=weather_data["main"]["temp"], description=weather_data["weather"][0]["description"], city=weather_data["name"])
                weather_obj.save()
            except:
                pass