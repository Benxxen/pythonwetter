# -*- coding: UTF-8 -*-
__author__ = 'patrick'
from mysite.models import Weather
import yweather
import urllib
import hashlib
from xml.dom import minidom
from time import strftime

WEATHER_URLY = 'http://xml.weather.yahoo.com/forecastrss?w=%s&u=c'
WEATHER_NSY = 'http://xml.weather.yahoo.com/ns/rss/1.0'

cityarray = ['Potsdam', 'Berlin', 'Hamburg', 'Brandenburg, Havel']

for city in cityarray:
    ########### Yahoo ###########
    client = yweather.Client()
    woeid = client.fetch_woeid(city)
    url = WEATHER_URLY % woeid
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = []
    ycondition = dom.getElementsByTagNameNS(WEATHER_NSY, 'condition')[0]
    yastronomy = dom.getElementsByTagNameNS(WEATHER_NSY, 'astronomy')[0]
    ywind = dom.getElementsByTagNameNS(WEATHER_NSY, 'wind')[0]
    yunits = dom.getElementsByTagNameNS(WEATHER_NSY, 'units')[0]
    ywindspeed = str(ywind.getAttribute('speed'))
    ywindspeed = int(ywindspeed[:-3])
    winddir = int(ywind.getAttribute('direction'))
    unit = yunits.getAttribute('temperature')
    temperature = ycondition.getAttribute('temp')
    condition = str(ycondition.getAttribute('text'))
    code = int(ycondition.getAttribute('code'))
    title = dom.getElementsByTagName('title')[0].firstChild.data[16:]
    winddir = 'N'
    if winddir <= 23:
        winddir = 'N'
    elif winddir <= 67:
        winddir = 'NE'
    elif winddir <= 113:
        winddir = 'E'
    elif winddir <= 158:
        winddir = 'SE'
    elif winddir <= 203:
        winddir = 'S'
    elif winddir <= 248:
        winddir = 'SW'
    elif winddir <= 293:
        winddir = 'W'
    elif winddir <= 338:
        winddir = 'NW'
    else:
        winddir = 'no'
    ######################
    ########### Wetter.com ###########
    projektname = "pythonwetterfhb"
    apikey = "c5aa08dea1427f7a5a90762ccca6d430"
    checksum = hashlib.md5(projektname + apikey + city).hexdigest()
    urlstart = "http://api.wetter.com/location/name/search/"
    cityURL = urlstart + city + "/project/" + projektname + "/cs/" + checksum
    url = cityURL
    dom = minidom.parse(urllib.urlopen(url))
    citycode = dom.getElementsByTagName('city_code')[0].firstChild.data
    client = yweather.Client()
    apiurl = "http://api.wetter.com/forecast/weather/city/"
    projektname = "pythonwetterfhb"
    apikey = "c5aa08dea1427f7a5a90762ccca6d430"
    checksum = hashlib.md5(projektname + apikey + citycode).hexdigest()
    url = apiurl + citycode + "/project/" + projektname + "/cs/" + checksum
    dom = minidom.parse(urllib.urlopen(url))
    wwindspeed = dom.getElementsByTagName('ws')[4].firstChild.data
    wwinddir = dom.getElementsByTagName('wd_txt')[4].firstChild.data
    wsunrise = 'keine Angabe'
    wsunset = 'keine Angabe'
    wtemp = 'keine Angabe'
    wcode = dom.getElementsByTagName('w')[4].firstChild.data
    wtitle = dom.getElementsByTagName('name')[0].firstChild.nodeValue + ", " + citycode[0:2]
    wcondition = dom.getElementsByTagName('w_txt')[4].firstChild.data
    wtemperature = dom.getElementsByTagName('tx')[4].firstChild.data
    w1 = Weather(datum=strftime("%Y-%m-%d"), stadt=title, anbieter='Yahoo', wetter=condition, tagestemperatur=temperature, einheit=unit, kondition=code, windgeschwindigkeit=ywindspeed, windrichtung=winddir)
    w1.save()
    w2 = Weather(datum=strftime("%Y-%m-%d"), stadt=wtitle, anbieter='Wetter.com', wetter=wcondition, tagestemperatur=wtemperature, einheit=unit, kondition=wcode, windgeschwindigkeit=wwindspeed, windrichtung=wwinddir)
    w2.save()

print "Fertig"