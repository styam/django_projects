from django.urls import path, include

from weather_app.views import WeatherAppViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', WeatherAppViewSet, basename='weather-data')


urlpatterns = [
    path('weather/', include(router.urls)),
]
