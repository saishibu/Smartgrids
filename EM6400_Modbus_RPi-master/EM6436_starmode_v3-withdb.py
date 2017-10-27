#ModBUS Communication between Schneider EM6436 Meter and Raspberry Pi
#First beta version.
#The meter is set with the following settings
#Communication : (RS484 to RS232 to USB) - BaudRate = 19200, Parity = N, Stopbits = 1, Device ID=1 (Hardcode in meter)
#Electical Settings: APri:50, Asec: 5, VPri: 415, Vsec:415, SYS: Star
#To use the meter in Single Phase mode, Some address has to be commented.
#This program was tested on RPi3 running Rasbian Jessie Pixel from Noobs V2
#Debian Kernel = Linux raspberrypi 4.4.38-v7+ #938 SMP Thu Dec 15 15:22:21 GMT 2016 armv7l GNU/Linux

#Additional Packages: pymodbus,pyserial. (available in pyPi repo)
#V1.0b Feb2,2017
#Code by Sai Shibu (AWNA/058/15)
#Copyrights AmritaWNA Smartgrid Tag

import time
import pymodbus 
import serial
import pymysql
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer

#Diagnosis messages not requires.

#from pymodbus.diag_message import *
#from pymodbus.file_message import *
#from pymodbus.other_message import *
#from pymodbus.mei_message import *

#Endian library for decoding HEX to Float
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder as decode
from pymodbus.payload import BinaryPayloadBuilder as builder


#logging not required. 
#import logging
#logging.basicConfig()
#log=logging.getLogger()
#log.setLevel(logging.DEBUG)

#EM6436 is defined as client
client = ModbusClient(method ='rtu',port='/dev/ttyUSB0',timeout=0.05) 
client.connect()
conn =pymysql.connect(database="SGL",user="root",password="root",host="localhost")
print("DB Open Successful\n")
cur=conn.cursor()
while 1:
	print "new set"
	
####################################################
#Read Whole Block (Bugs while decoding with Endian!!!)
#	T_RMS=client.read_holding_registers(0xbb8,20,unit=1)
#	R_RMS=client.read_holding_registers(0xbd6,20,unit=1) #Total R Phase RMS Block
#	Y_RMS=client.read_holding_registers(0xbd6,20,unit=1) #Total Y Phase RMS Block
#	B_RMS=client.read_holding_registers(0xbd6,20,unit=1) #Total B Phase RMS Block
#####################################################

	#Current Values
	A=client.read_holding_registers(3912,2,unit=1)
	A1=client.read_holding_registers(3928,2,unit=1) 
	A2=client.read_holding_registers(3942,2,unit=1) 
	A3=client.read_holding_registers(3956,2,unit=1) 

        A_d = decode.fromRegisters(A.registers, endian=Endian.Big)
        A_d ={'float':A_d.decode_32bit_float(),}

        A1_d = decode.fromRegisters(A1.registers, endian=Endian.Big)
        A1_d ={'float':A1_d.decode_32bit_float(),}

        A2_d = decode.fromRegisters(A2.registers, endian=Endian.Big)
        A2_d ={'float':A2_d.decode_32bit_float(),}

        A3_d = decode.fromRegisters(A3.registers, endian=Endian.Big)
        A3_d ={'float':A3_d.decode_32bit_float(),}

#####################################################
	#Voltage Values
	VLL=client.read_holding_registers(3908,2,unit=1) 
	VLN=client.read_holding_registers(3910,2,unit=1)
	V12=client.read_holding_registers(3924,2,unit=1) 
	V23=client.read_holding_registers(3938,2,unit=1) 
	V31=client.read_holding_registers(3952,2,unit=1) 
	V1=client.read_holding_registers(3926,2,unit=1) 
	V2=client.read_holding_registers(3940,2,unit=1) 
	V3=client.read_holding_registers(3954,2,unit=1) 

        VLN_d = decode.fromRegisters(VLN.registers, endian=Endian.Big)
        VLN_d ={'float':VLN_d.decode_32bit_float(),}

        VLL_d = decode.fromRegisters(VLL.registers, endian=Endian.Big)
        VLL_d ={'float':VLL_d.decode_32bit_float(),}

        V12_d = decode.fromRegisters(V12.registers, endian=Endian.Big)
        V12_d ={'float':V12_d.decode_32bit_float(),}

        V23_d = decode.fromRegisters(V23.registers, endian=Endian.Big)
        V23_d ={'float':V23_d.decode_32bit_float(),}

        V31_d = decode.fromRegisters(V31.registers, endian=Endian.Big)
        V31_d ={'float':V31_d.decode_32bit_float(),}

        V1_d = decode.fromRegisters(V1.registers, endian=Endian.Big)
        V1_d ={'float':V1_d.decode_32bit_float(),}

        V2_d = decode.fromRegisters(V2.registers, endian=Endian.Big)
        V2_d ={'float':V2_d.decode_32bit_float(),}

        V3_d = decode.fromRegisters(V3.registers, endian=Endian.Big)
        V3_d ={'float':V3_d.decode_32bit_float(),}

######################################################
	#Power Values 
	#NOTE: EM6436 does not give VAR Values!!!

	W=client.read_holding_registers(3902,2,unit=1) 
	W1=client.read_holding_registers(3918,2,unit=1)  
	W2=client.read_holding_registers(3932,2,unit=1)  
	W3=client.read_holding_registers(3946,2,unit=1)
	VA=client.read_holding_registers(3900,2,unit=1)
	VA1=client.read_holding_registers(3916,2,unit=1) 
	VA2=client.read_holding_registers(3930,2,unit=1) 
	VA3=client.read_holding_registers(3944,2,unit=1) 

        W_d = decode.fromRegisters(W.registers, endian=Endian.Big)
        W_d ={'float':W_d.decode_32bit_float(),}

        W1_d = decode.fromRegisters(W1.registers, endian=Endian.Big)
        W1_d ={'float':W1_d.decode_32bit_float(),}

        W2_d = decode.fromRegisters(W2.registers, endian=Endian.Big)
        W2_d ={'float':W2_d.decode_32bit_float(),}

        W3_d = decode.fromRegisters(W3.registers, endian=Endian.Big)
        W3_d ={'float':W3_d.decode_32bit_float(),}

        VA_d = decode.fromRegisters(VA.registers, endian=Endian.Big)
        VA_d ={'float':VA_d.decode_32bit_float(),}

        VA1_d = decode.fromRegisters(VA1.registers, endian=Endian.Big)
        VA1_d ={'float':VA1_d.decode_32bit_float(),}

        VA2_d = decode.fromRegisters(VA2.registers, endian=Endian.Big)
        VA2_d ={'float':VA2_d.decode_32bit_float(),}

        VA3_d = decode.fromRegisters(VA3.registers, endian=Endian.Big)
        VA3_d ={'float':VA3_d.decode_32bit_float(),}

######################################################
	#Power Factor Values
	PF=client.read_holding_registers(3906,2,unit=1)
	PF1=client.read_holding_registers(3922,2,unit=1) 
	PF2=client.read_holding_registers(3936,2,unit=1) 
	PF3=client.read_holding_registers(3950,2,unit=1) 

        PF_d = decode.fromRegisters(PF.registers, endian=Endian.Big)
        PF_d ={'float':PF_d.decode_32bit_float(),}

        PF1_d = decode.fromRegisters(PF1.registers, endian=Endian.Big)
        PF1_d ={'float':PF1_d.decode_32bit_float(),}

        PF2_d = decode.fromRegisters(PF2.registers, endian=Endian.Big)
        PF2_d ={'float':PF2_d.decode_32bit_float(),}

        PF3_d = decode.fromRegisters(PF3.registers, endian=Endian.Big)
        PF3_d ={'float':PF3_d.decode_32bit_float(),}

######################################################
	#Frequency Value
	F=client.read_holding_registers(3914,2,unit=1)
	F_d = decode.fromRegisters(F.registers, endian=Endian.Big)
        F_d ={'float':F_d.decode_32bit_float(),}
######################################################
	#Energy Value
	VAH=client.read_holding_registers(3958,2,unit=1) 
	WH=client.read_holding_registers(3960,2,unit=1) 
	VAH_d = decode.fromRegisters(VAH.registers, endian=Endian.Big)
        VAH_d ={'float':VAH_d.decode_32bit_float(),}
        WH_d = decode.fromRegisters(WH.registers, endian=Endian.Big)
        WH_d ={'float':WH_d.decode_32bit_float(),}
######################################################
	#Power Interruptions count
	intr=client.read_holding_registers(3998,2,unit=1) 
	intr_d = decode.fromRegisters(intr.registers, endian=Endian.Big)
        intr_d ={'16uint':intr_d.decode_16bit_uint(),}
 
######################################################

        print "-" * 100
        timestamp = time.strftime('%H:%M:%S %d-%m-%Y')
        print timestamp
	print "Current Values"

	for i, value in A_d.iteritems():
		print value
		A=value

        for i, value in A1_d.iteritems():
                print value
		A1=value

        for i, value in A2_d.iteritems():
                print value
		A2=value

        for i, value in A3_d.iteritems():
                print value
		A3=value
	A_RMS=[A,A1,A2,A3]

	
	
	print "-" * 100
	print "Voltage Values"

        for i, value in VLL_d.iteritems():
                print value
		VLL=value

        for i, value in VLN_d.iteritems():
                print value
		VLN=value

        for i, value in V12_d.iteritems():
                print value
		V12=value

        for i, value in V23_d.iteritems():
                print value
		V23=value

        for i, value in V31_d.iteritems():
                print value
		V31=value

        for i, value in V1_d.iteritems():
                print value
		V1=value

        for i, value in V2_d.iteritems():
                print value
		V2=value

        for i, value in V3_d.iteritems():
                print value
		V3=value
        V_RMS=[VLL,VLN,V12,V23,V31,V1,V2,V3]
	print "-" * 100
	print "Power Factor Values"

        for i, value in PF_d.iteritems():
                print value
                PF=value
        for i, value in PF1_d.iteritems():
                print value
                PF1=value
        for i, value in PF2_d.iteritems():
                print value
                PF2=value
        for i, value in PF3_d.iteritems():
                print value
                PF3=value
        PF_RMS=[PF,PF1,PF2,PF3]
	print "-" * 100
	print "Frequency Value"

        for i, value in F_d.iteritems():
                print value
                F=value
	print "-" * 100
	print "Power Values"

        for i, value in W_d.iteritems():
                print value
                W=value

        for i, value in W1_d.iteritems():
                print value
                W1=value

        for i, value in W2_d.iteritems():
                print value
                W2=value

        for i, value in W3_d.iteritems():
                print value
                W3=value
        W_RMS=[W,W1,W2,W3]
        for i, value in VA_d.iteritems():
                print value
                VA=value

        for i, value in VA1_d.iteritems():
                print value
                VA1=value

        for i, value in VA2_d.iteritems():
                print value
                VA2=value

        for i, value in VA3_d.iteritems():
                print value
                VA3=value

        VA_RMS=[VA,VA1,VA2,VA3]
	print "-" * 100
	print "Energy Value"

        for i, value in VAH_d.iteritems():
                print value
                VAH=value
        for i, value in WH_d.iteritems():
                print value
                WH=value
	print "-" * 100
	print "interruption"

        for i, value in intr_d.iteritems():
                print value
                intr=value

	print "-" * 100
	meter="3phs"
	data={'meter':meter,
              'A':A, 'A1':A1,'A2':A2,'A3':A3,
              'VLL':VLL,'VLN':VLN,'V12':V12,'V23':V23,'V31':V31,'V1':V1,'V2':V2,'V3':V3,
              'PF':PF,'PF1':PF1,'PF2':PF2,'PF3':PF3,
              'F':F,
              'W':W,'W1':W1,'W2':W2,'W3':W3,
              'VA':VA,'VA1':VA,'VA2':VA2,'VA3':VA3,
              'VAH':VAH,'WH':WH}

#todb

        cur.execute("""INSERT INTO 3phSource(meter,A,A1,A2,A3,VLL,VLN,V12,V23,V31,V1,V2,V3,PF,PF1,PF2,PF3,F,W,W1,W2,W3,VA,VA1,VA2,VA3,VAh,Wh) VALUES (%(meter)s,%(A)s,%(A1)s,%(A2)s,%(A3)s,%(VLL)s,%(VLN)s,%(V12)s,%(V23)s,%(V31)s,%(V1)s,%(V2)s,%(V3)s,%(PF)s,%(PF1)s,%(PF2)s,%(PF3)s,%(F)s,%(W)s,%(W1)s,%(W2)s,%(W3)s,%(VA)s,%(VA1)s,%(VA2)s,%(VA3)s,%(VAH)s,%(WH)s)""",data)
        conn.commit()
conn.close()
client.close()

