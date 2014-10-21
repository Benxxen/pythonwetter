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

client = yweather.Client()
woeid = client.fetch_woeid('Berlin')

url = WEATHER_URLY % woeid
dom = minidom.parse(urllib.urlopen(url))
forecasts = []
ycondition = dom.getElementsByTagNameNS(WEATHER_NSY, 'condition')[0]
yastronomy = dom.getElementsByTagNameNS(WEATHER_NSY, 'astronomy')[0]
ywind = dom.getElementsByTagNameNS(WEATHER_NSY, 'wind')[0]
yunits = dom.getElementsByTagNameNS(WEATHER_NSY, 'units')[0]

windspeed = str(ywind.getAttribute('speed'))
winddir = int(ywind.getAttribute('direction'))
unit = yunits.getAttribute('temperature'),
yastronomy.getAttribute('sunrise'),
temperature = ycondition.getAttribute('temp'),
yastronomy.getAttribute('sunset'),
condition = ycondition.getAttribute('text')
ycondition.getAttribute('temp'),
code = str(ycondition.getAttribute('code')),
forecasts,
dom.getElementsByTagName('title')[0].firstChild.data

if winddir <= 23:
    winddir = 'N'
elif winddir <= 67:
    winddir =  'NE'
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
    winddir = 'ni'

connection = psycopg2.connect(database='pythonwetter', user=os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'], password=os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'], host=os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'], port=os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'])
cursor = connection.cursor()
cursor.execute("INSERT INTO mysite_weather (Datum, Stadt, Anbieter, Wetter, Tagestemperatur, Einheit, Kondition, Windgeschwindigkeit, Windrichtung) VALUES ('2014-10-21','Berlin','Yahoo',%s,%s,%s,%s,&s,%s)", (condition, temperature, unit, code, windspeed, winddir ))
connection.commit()
connection.close()