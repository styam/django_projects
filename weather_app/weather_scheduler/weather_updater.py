from apscheduler.schedulers.background import BackgroundScheduler

from weather_app.views import WeatherAppViewSet


def start():
  scheduler = BackgroundScheduler()
  weather = WeatherAppViewSet()
  scheduler.add_job(weather.save_weather_data, "interval", seconds=5, id="weather_001", replace_existing=True)
  scheduler.start()
