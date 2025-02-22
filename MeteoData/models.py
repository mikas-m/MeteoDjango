from django.db import models

class MeteoData(models.Model):
    region = models.CharField(max_length=100)
    station = models.CharField(max_length=100)
    elevation = models.IntegerField()
    date = models.DateField()
    time = models.IntegerField()
    temperature = models.DecimalField(max_digits=10, decimal_places=1)
    temperature_max = models.DecimalField(max_digits=10, decimal_places=1)
    temperature_min = models.DecimalField(max_digits=10, decimal_places=1)
    temperature_trend_hour = models.DecimalField(max_digits=10, decimal_places=1)
    temperature_trend_3hours = models.DecimalField(max_digits=10, decimal_places=1)
    temperature_trend_day = models.DecimalField(max_digits=10, decimal_places=1)
    precipitation = models.DecimalField(max_digits=10, decimal_places=1)
    precipitation_hour = models.DecimalField(max_digits=10, decimal_places=1)
    precipitation_trend_hour = models.DecimalField(max_digits=10, decimal_places=1)
    precipitation_trend_3hours = models.DecimalField(max_digits=10, decimal_places=1)
    precipitation_day = models.DecimalField(max_digits=10, decimal_places=1)
    precipitation_trend_day = models.DecimalField(max_digits=10, decimal_places=1)
    precipitation_month = models.DecimalField(max_digits=10, decimal_places=1)
    pressure = models.DecimalField(max_digits=10, decimal_places=1)
    pressure_trend_hour = models.DecimalField(max_digits=10, decimal_places=1)
    pressure_trend_3hours = models.DecimalField(max_digits=10, decimal_places=1)
    pressure_trend_day = models.DecimalField(max_digits=10, decimal_places=1)
    humidity = models.DecimalField(max_digits=10, decimal_places=1)
    humidity_trend_hour = models.DecimalField(max_digits=10, decimal_places=1)
    humidity_trend_3hours = models.DecimalField(max_digits=10, decimal_places=1)
    humidity_trend_day = models.DecimalField(max_digits=10, decimal_places=1)
    wind_direction = models.CharField(max_length=10)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=1)
    wind_max = models.DecimalField(max_digits=10, decimal_places=1)
    wind_gust = models.DecimalField(max_digits=10, decimal_places=1)
    wind_gust_max = models.DecimalField(max_digits=10, decimal_places=1)
    wind_gust_max_dir = models.CharField(max_length=10)
    wind_chill = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return f"{self.station} -> Region - {self.region}"