import serial
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=1)

while 1:
	ser.write('xbee\r\n')
	
