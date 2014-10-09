# -*- coding: iso-8859-15 -*-
from django.shortcuts import render
from PythonWetter.getweather import yahoowetter
from PythonWetter.getweather import wettercomwetter
from xml.dom import minidom
import yweather
import hashlib
import urllib


def get_weather_list(request):
    ########## Auslesen der Stadt aus der URL (GET) ##########
    city = request.GET.get('city', '')
    print(city)
    if city == '':
        city = 'Berlin'

    ########## Suche nach der Stadt bei Wetter.com mit Auswertung der XML-Datei ##########
    projektname = "pythonwetterfhb"
    apikey = "c5aa08dea1427f7a5a90762ccca6d430"
    checksum = hashlib.md5(projektname + apikey + city).hexdigest()

    urlstart = "http://api.wetter.com/location/name/search/"
    cityURL = urlstart + city + "/project/" + projektname + "/cs/" + checksum
    url = cityURL
    dom = minidom.parse(urllib.urlopen(url))
    print url
    citycode = dom.getElementsByTagName('city_code')[0].firstChild.data
    client = yweather.Client()

    ########## Umwandeln der Stadt in eine Where on Earty ID (WOEID) ##########
    woe = client.fetch_woeid(city)
    weather_listy = yahoowetter(woe)
    weather_listw = wettercomwetter(citycode)
    return render(request, 'weather_list.html', {'page_title': 'Wetter in Python', 'yahoo_wetter': weather_listy,
                                                 'wetter_com': weather_listw})
