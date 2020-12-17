from django.db import models


class Weather(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.timestamp} {self.temperature} {self.description} {self.city}"
