# -*- coding: iso-8859-15 -*-
from django.shortcuts import render
from pythonwetter.getweather import yahoowetter
from pythonwetter.getweather import wettercomwetter
from pythonwetter.serializers import *
from rest_framework import viewsets, filters
from pythonwetter.functions import stadtidw
from pythonwetter.functions import stadtidy

def get_weather_list(request):

########## Auslesen der Stadt aus der URL (GET) ##########
    city = request.GET.get('city', '')
    if city == '':
        city = 'Berlin'

    warn = ""
    try:
        woe = stadtidy(city)
        citycode = stadtidw(city)
    except:
        city = 'Berlin'
        woe = stadtidy(city)
        citycode = stadtidw(city)
        warn = "Die gesuchte Stadt konnte leider nicht gefunden werden. Bitte waehlen Sie eine andere Stadt!"


    weather_listy = yahoowetter(woe)
    weather_listw = wettercomwetter(citycode)
    return render(request, 'weather_list.html', {'page_title': 'Wetter in Python', 'yahoo_wetter': weather_listy,
                                                 'wetter_com': weather_listw, 'warning': warn},)


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('datum', 'stadt')