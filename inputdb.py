__author__ = 'patrick'
import psycopg2
import os
import yweather
import urllib
import hashlib
from xml.dom import minidom
from django.shortcuts import render

WEATHER_URLY = 'http://xml.weather.yahoo.com/forecastrss?w=%s&u=c'
WEATHER_NSY = 'http://xml.weather.yahoo.com/ns/rss/1.0'

woeid = client.fetch_woeid('Berlin')

url = WEATHER_URLY % woeid
dom = minidom.parse(urllib.urlopen(url))
forecasts = []
ycondition = dom.getElementsByTagNameNS(WEATHER_NSY, 'condition')[0]
yastronomy = dom.getElementsByTagNameNS(WEATHER_NSY, 'astronomy')[0]
ywind = dom.getElementsByTagNameNS(WEATHER_NSY, 'wind')[0]
yunits = dom.getElementsByTagNameNS(WEATHER_NSY, 'units')[0]

ywind.getAttribute('speed'),
ywind.getAttribute('direction'),
yunits.getAttribute('temperature'),
yastronomy.getAttribute('sunrise'),
ycondition.getAttribute('temp'),
yastronomy.getAttribute('sunset'),
ycondition.getAttribute('text'),
ycondition.getAttribute('temp'),
ycondition.getAttribute('code'),
forecasts,
dom.getElementsByTagName('title')[0].firstChild.data


connection = psycopg2.connect(os.environ['OPENSHIFT_APP_NAME'])
cursor = connection.cursor()
cursor.execute("INSERT INTO PythonWetter_weather (Datum, Stadt, Anbieter, Wetter, Tagestemperatur, Einheit, Kondition, Windgeschwindigkeit, Windrichtung) VALUES ('2014-10-14','Potsdam','Yahoo','%s',10,'C',30,60,'SW'),", ycondition.getAttribute('text'),)
connection.commit()
connection.close()