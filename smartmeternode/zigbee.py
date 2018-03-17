import serial
ser = serial.Serial('/dev/ttyUSB1', 9600,timeout=.5)

def sendbee(data):
	ser.write(data+'\r\n')
	print "Zigbee packet sent"
