#!/usr/bin/python

#python script to read from smartmeter(Maxim) connected to USB port, calculates real, reactive and apparent power.
#script by Sreevalsa(Smartmeter data fetch),Nikhitha(Algorithm) and Sai Shibu(Database).
#Version 3.0 beta July 12,2017

#Changelogs:
#	Added MySQL Database links
#	Added Algorithms
#	Bugfix, where the meter readings show last reading in case of power falure
#	Clean ups
#	Math error fixed for reactive power

#Note: Start TCP Server before running this code
#To Disable TCP, comment TCP commands in this Program
#Edit TCP Properties in tcp_meternode.py file

########################################################################################################################################################################################################################################################################
#import all necessory packages and algorithms

import serial
import time
import re
import operator
import math
import json
import pymysql
import pymysql.cursors
#import sys
#sys.path.insert(0,'/path/to/home/pi/Smartgrids/smartmeternode')
from Algo import frequency
from Algo import voltage
from Algo import temperature
from Algo import overload
from Algo import linebreakage
#import support
#from tcp_meternode import send
#from dbwrite import todb

#establish Serial connection to maxim meter
port=serial.Serial("/dev/ttyUSB0",baudrate=9600,timeout=.1)

conn = pymysql.connect(db="INTELLIGENTNODE", user="root", password="root", host="localhost",cursorclass=pymysql.cursors.DictCursor)
print "Opened database successfully"


#variable declaration

testarr=[]
node_data=dict()
node_error=dict()
cmnd1='m'
cmnd2=0

cmnd=cmnd1+str(cmnd2)
j=0

#data fetch loop
while 1:

        for i in range(9):
                port.write(cmnd)
                port.write("\r")
                rcv =port.read(90)
                rcv=rcv.replace('L1','')
                l=list(rcv)
                if cmnd2<10:
                        l[0:2]=[]
                if cmnd2>9:
                        l[0:3]=[]
                rcv="".join(l)
                cmnd2+=1
                if cmnd2 == 4:
                        cmnd2=6
		elif cmnd2 ==8:
                        cmnd2=11
                elif cmnd2 ==12:
                        cmnd2=15
                elif cmnd2==17:
                        cmnd2=0

                cmnd=cmnd1+str(cmnd2)
                #print rcv
		g=map(lambda v: float(v) if '.' in v else int(v),re.findall(r'\d+(?:\.\d+)?',rcv))
		testarr.append(g)
        test = reduce(operator.add, testarr)

#meter data stored in variables
        m0_data=test[0]
        m1_data=test[1]
        m2_data=test[2]
        m3_data=test[3]
        m6_data=test[4]
        m7_data=test[5]
        m11_data=test[6]
        m15_data=test[7]
        m16_data=test[8]
#power calculation in real time
	realpower=m15_data*m16_data*m11_data
	if (m11_data<1):
		reactivepower=m15_data*m16_data*(math.sin(math.acos(m11_data)))       
	else:
		reactivepower=0

	apparentpower=m15_data*m16_data
	timestamp=time.asctime(time.localtime(time.time()))

#Algorithms
# 1)frequency check
	
	freq_error = frequency(m2_data)	
# 2)voltage check
	volt_error = voltage(m16_data)
# 3)temperature check
	temp_error = temperature(m1_data)
#4) Overload check
	overload_error = overload(apparentpower)
#5) Linebreakage check
	line_error = linebreakage(m2_data,m16_data)

#json format

	node_data={
		'time':timestamp,
                'meter':m0_data,
                'temperature':m1_data,
               	'freq':m2_data,
		'penergy':m3_data,
                'qenergy':m6_data,
                'senergy':m7_data,
                'cospi':m11_data,
                'irms':m15_data,
                'vrms':m16_data,
                'ppower':realpower,
                'qpower':reactivepower,
                'spower':apparentpower,
	 }

	node_event={'frequency error':freq_error,'voltage status':volt_error,'temperature status':temp_error,'overload status':overload_error,'line breakage':line_error}
        
	json_data = json.dumps(node_data)
	json_event = json.dumps(node_event)

	print json_data
	print json_event

#Store to SQL
	cursor= conn.cursor()

	sql= "INSERT INTO nodedata(meter,temperature,freq,penergy,qenergy,senergy,cospi,irms,vrms,ppower,qpower,spower) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
	cursor.execute(sql,(m0_data,m1_data,m2_data,m3_data,m6_data,m7_data,m11_data,m15_data,m16_data,realpower,reactivepower,apparentpower))

	sql_events= "INSERT INTO nodeevents(meter,frequency_status,voltage_status,temp_status,overload_status,line_status) VALUES (%s,%s,%s,%s,%s,%s);"
	cursor.execute(sql_events,(m0_data,freq_error,volt_error,temp_error,overload_error,line_error))

	#todb(data)
	conn.commit()

#TCP Data transmission

#	send(json_data)

#Reset Variables
	g=0;test=0;testarr=[]
	m0_data=0;m1_data=0;m2_data=0;m3_data=0;m11_data=0;m6_data=0;m7_data=0;m15_data=0;m16_data=0;realpower=0;reactivepower=0;apparentpower=0;
	freq_error=0;volt_error=0;temp_error=0;overload_error=0;line_error=0;
