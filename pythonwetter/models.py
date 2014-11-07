# -*- coding: utf-8 -*-
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
    windgeschwindigkeit = models.IntegerField(max_length=5)
    windrichtung = models.CharField(max_length=2)

    def __str__(self):
        return str(self.datum) + ", " + self.stadt + ", " + self.anbieter