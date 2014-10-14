"""
Kardinalitaetsproblematik in Django
"""

from django.db import models


class Weather(models.Model):
    datum = models.DateField(max_length=16)
    stadt = models.CharField(max_length=32)
    anbieter = models.CharField(max_length=32)
    wetter = models.CharField(max_length=16)
    tagestemperatur = models.IntegerField(max_length=3)
    einheit = models.CharField(max_length=1)
    kondition = models.IntegerField(max_length=4)
    windgeschwindigkeit = models.IntegerField(max_length=3)
    windrichtung = models.CharField(max_length=2)


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

