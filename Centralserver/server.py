import os
import socket
import json
import yaml
from dbwrite import todb
data=dict()


s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)

host = '172.20.4.132'

port = 123

s.bind((host, port))

s.listen(5)
while True:
	c, addr = s.accept()
	data =c.recv(1024)
	print ('Got connection from', addr)
	print '\n'
	print data
	json_data = yaml.load(data)
	print json_data
	todb(json_data)
	
