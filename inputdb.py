__author__ = 'patrick'
import sqlite3
import os

connection = sqlite3.connect(os.environ['OPENSHIFT_APP_NAME'])
cursor = connection.cursor()
cursor.execute("INSERT INTO PythonWetter_weather (Datum, Stadt, Anbieter, Wetter, Tagestemperatur, Einheit, Kondition, Windgeschwindigkeit, Windrichtung) VALUES ('2014-10-14','Potsdam','Yahoo','Rainy',10,'C',30,60,'SW')")
connection.commit()
connection.close()