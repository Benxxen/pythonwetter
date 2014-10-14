"""
Kardinalitaetsproblematik in Django
"""

from django.db import models


class Weather(models.Model):
    Datum = models.DateField(max_length=16)
    Stadt = models.CharField(max_length=32)
    Anbieter = models.CharField(max_length=32)
    Wetter = models.CharField(max_length=16)
    Tagestemperatur = models.IntegerField(max_length=3)
    Einheit = models.CharField(max_length=1)
    Kondition = models.IntegerField(max_length=4)
    Windgeschwindigkeit = models.IntegerField(max_length=3)
    Windrichtung = models.CharField(max_length=2)


# class PLZ(models.Model):
#

# class Forecast(models.Model):
#     day = models.CharField(max_length=8)
#     date = models.CharField(max_length=32)
#     templow = models.IntegerField(max_length=8)
#     temphigh = models.IntegerField(max_length=8)
#     wetter = models.CharField(max_length=32)
#     code = models.IntegerField(max_length=2)
#
#     def __str__(self):
#         return "{} {} {}".format(self.wetter, self.city, self.temperaturemax, self.temperaturemin)


    #location_region = models.CharField(max_length=10)
    #location_country = models.CharField(max_length=32)
    #units_distance = models.CharField(max_length=2)
    #units_pressure = models.CharField(max_length=2)
    #units_speed = models.CharField(max_length=4)
    #wind_chill = models.IntegerField(max_length=8)

    #astronomy_sunrise = models.CharField(max_length=8)
    #astronomy_sunset = models.CharField(max_length=8)

    #condition_temp = models.CharField(max_length=3)
    #condition_date = models.CharField(max_length=20)

