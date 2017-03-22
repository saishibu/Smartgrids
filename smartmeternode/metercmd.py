#!/usr/bin/python

#python script to read from smartmeter(Maxim) connected to USB port, calculates real, reactive and a$
#script by Sreevalsa and Sai Shibu
#Version 2.0 beta July 13,2016
#Changelogs:
#	Added PostgreSQL Database links
#	Added Algorithms
#	Bugfix, where the meter readings show last reading in case of power falure
#	Clean ups
#	TCP Communication Setup

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
import psycopg2
from tcp_meternode import send
from dbwrite import todb

#establish Serial connection to maxim meter
port=serial.Serial("/dev/ttyUSB0",baudrate=9600,timeout=.1)

#variable declaration
event="nill"
testarr=[]
data=dict()
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
	reactivepower=m15_data*m16_data*(math.sin(math.acos(m11_data)))       
	apparentpower=m15_data*m16_data
	timestamp=time.asctime(time.localtime(time.time()))

#Algorithms
# 1)frequency check
	if m2_data !=50:
		event1 = "frequency error & "
	else:
		event1 = "Frequency check clear"
# 2)Power factor check
	if m11_data !=1:
		event2 = "Lagging Power Factor"
	else:
		event2 = "Power factor check clear"
# 3)
# 4)

	event = event1+event2

#json format

	data={
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
       		'event':event
	 }
        
	json_data = json.dumps(data)
	print json_data

#Store to SQL

        todb(data)

#TCP Data transmission

	send(json_data)

#Reset Variables
	g=0;test=0;testarr=[]
	m0_data=0;m1_data=0;m2_data=0;m3_data=0;m11_data=0;m6_data=0;m7_data=0;m15_data=0;m16_data=0;realpower=0;reactivepower=0;apparentpower=0;event="nill"
