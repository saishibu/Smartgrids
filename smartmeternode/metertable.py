# -*- coding: utf-8 -*-
#!/usr/bin/python

#PYTHON SCRIPT TO CREATE A TABLE 'meter' IN POSTGRESQL DATABASE 'smartmeternode'
#Sai Shibu, V1.0 24/06/16
#(c) Amrita WNA

#NOTE1: Database has to be created before running this file. (createdb smartmeternode -U postgres)
#NOTE2: THIS PROGRAM WILL DELETE PREVIOUS DATA ON THE DATABASE



import psycopg2

conn = psycopg2.connect(database="smartmeternode", user="postgres", password="amma", host="localhost", port="5432")

print "Opened database successfully"

cur = conn.cursor()

#cur.execute('DROP TABLE metertable;') #uncomment this line if âtable exist error occurs

#cur.execute('CREATE TABLE metertable (ID      SERIAL  PRIMARY KEY	NOT NULL,meter	INT	NOT NULL,temperature	FLOAT	NOT NULL,freq	FLOAT	NOT NULL,penergy	INT	NOT NULL,qenergy	INT	 NOT NULL,senergy	INT	NOT NULL,cospi	FLOAT	NOT NULL,irms	FLOAT	NOT NULL,vrms	FLOAT	NOT NULL,ppower	FLOAT	 NOT NULL,qpower	FLOAT	NOT NULL,spower	FLOAT	NOT NULL,EVENT	TEXT	NOT NULL);')
cur.execute('CREATE TABLE metertable (ID      SERIAL  PRIMARY KEY,meter	INT	NOT NULL,temperature	FLOAT	NOT NULL,freq	FLOAT	NOT NULL,penergy	INT	NOT NULL,qenergy	INT	 NOT NULL,senergy	INT	NOT NULL,cospi	FLOAT	NOT NULL,irms	FLOAT	NOT NULL,vrms	FLOAT	NOT NULL,ppower	FLOAT	 NOT NULL,qpower	FLOAT	NOT NULL,spower	FLOAT	NOT NULL,EVENT	TEXT	NOT NULL);')

print "Table created successfully\n"
print "Now run metercmd.py\n"

