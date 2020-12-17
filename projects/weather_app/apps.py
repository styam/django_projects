from django.apps import AppConfig

class WeatherAppConfig(AppConfig):
    name = 'weather_app'

    def ready(self):
        from .weather_scheduler import weather_updater
        weather_updater.start()
