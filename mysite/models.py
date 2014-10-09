"""
Kardinalitaetsproblematik in Django
"""

from django.db import models

# Cat

#WAR VORHER BRAND

#
# class TemperatureMin(models.Model):
#     temperatureMin = models.IntegerField(max_length=8)
#
#     def __str__(self):
#         return self.TemperatureMin, self.temperatureMax
#
#
# class TemperatureMax(models.Model):
#     temperatureMax = models.IntegerField(max_length=32)
#
#     def __str__(self):
#         return self.TemperatureMax

class Weather(models.Model):
    location_city = models.CharField(max_length=32)
    location_region = models.CharField(max_length=10)
    location_country = models.CharField(max_length=32)
    units_temperature = models.CharField(max_length=1)
    units_distance = models.CharField(max_length=2)
    units_pressure = models.CharField(max_length=2)
    units_speed = models.CharField(max_length=4)
    wind_chill = models.IntegerField(max_length=8)
    wind_direction = models.IntegerField(max_length=8)
    wind_speed = models.IntegerField(max_length=8)
    astronomy_sunrise = models.CharField(max_length=8)
    astronomy_sunset = models.CharField(max_length=8)
    condition_text = models.CharField(max_length=16)
    condition_temp = models.CharField(max_length=3)
    condition_date = models.CharField(max_length=20)
    condition_code = models.IntegerField(max_length=2)

    def __str__(self):
        return self.location_city


# class PLZ(models.Model):
#

class Forecast(models.Model):
    day = models.CharField(max_length=8)
    date = models.CharField(max_length=32)
    templow = models.IntegerField(max_length=8)
    temphigh = models.IntegerField(max_length=8)
    wetter = models.CharField(max_length=32)
    code = models.IntegerField(max_length=2)

    def __str__(self):
        return "{} {} {}".format(self.wetter, self.city, self.temperaturemax, self.temperaturemin)
