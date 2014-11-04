__author__ = 'McDaemon'


from models import Weather
from rest_framework import serializers


class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = ('datum', 'stadt', 'anbieter', 'anbieter', 'wetter', 'tagestemperatur', 'einheit', 'kondition',
                 'windgeschwindigkeit', 'windrichtung', 'url')