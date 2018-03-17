import serial

ser = serial.Serial('/dev/ttyUSB1', 9600,timeout=.5)
while 1:
	incoming = ser.readline().strip()
	print 'Received Data : '+ incoming
	print type(incoming)	
