__author__ = 'patrick'
import psycopg2
import os

connection = psycopg2.connect(database=os.environ['OPENSHIFT_APP_NAME'], user=os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'], password=os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'], host=os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'], port=os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'])
cursor = connection.cursor()
cursor.execute("INSERT INTO mysite_weather (Datum, Stadt, Anbieter, Wetter, Tagestemperatur, Einheit, Kondition, Windgeschwindigkeit, Windrichtung) VALUES ('2014-10-14','Potsdam','Yahoo','Rainy',10,'C',30,60,'SW')")
connection.commit()
connection.close()