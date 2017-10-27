# -*- coding: utf-8 -*-
#!/usr/bin/python

#PYTHON SCRIPT TO CREATE A TABLE 'nodedata' IN MySQL DATABASE 'INTELLIGENTNODE'
#Sai Shibu, V2.0 12/07/17
#(c) Amrita WNA

#NOTE1: Database has to be created before running this file.
#NOTE2: THIS PROGRAM WILL DELETE PREVIOUS DATA ON THE DATABASE



import pymysql

conn = pymysql.connect(database="INTELLIGENTNODE", user="root", password="root", host="localhost")

print "Opened database successfully"

cur = conn.cursor()

#cur.execute('CREATE TABLE metertable (ID      SERIAL  PRIMARY KEY	NOT NULL,meter	INT	NOT NULL,temperature	FLOAT	NOT NULL,freq	FLOAT	NOT NULL,penergy	INT	NOT NULL,qenergy	INT	 NOT NULL,senergy	INT	NOT NULL,cospi	FLOAT	NOT NULL,irms	FLOAT	NOT NULL,vrms	FLOAT	NOT NULL,ppower	FLOAT	 NOT NULL,qpower	FLOAT	NOT NULL,spower	FLOAT	NOT NULL,EVENT	TEXT	NOT NULL);')

cur.execute('CREATE TABLE nodedata (ID      SERIAL  PRIMARY KEY,time CHAR not null, meter	INT	NOT NULL,temperature	FLOAT	NOT NULL,freq	FLOAT	NOT NULL,penergy	INT	NOT NULL,qenergy	INT	 NOT NULL,senergy	INT	NOT NULL,cospi	FLOAT	NOT NULL,irms	FLOAT	NOT NULL,vrms	FLOAT	NOT NULL,ppower	FLOAT	 NOT NULL,qpower	FLOAT	NOT NULL,spower	FLOAT	NOT NULL);')
#cur.execute('CREATE TABLE nodeevents (ID      SERIAL  PRIMARY KEY,meter	INT	NOT NULL,freq INT NOT NULL);')


print "Table created successfully\n"
print "Now run metercmd.py\n"

