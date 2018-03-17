import os
import socket
import json
from dbwrite import todb
import serial

data=dict()
error="NIL"

s = socket.socket()
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)

host = '192.168.1.106'

port = 123

s.bind((host, port))

s.listen(5)
while True:
	c, addr = s.accept()
	data =c.recv(1024)
	print ('Got connection from', addr)
	print '\n'
	print data
	json_data = json.loads(data)
	print json_data
	todb(json_data)
	error = ser.readline().strip()
	print error
