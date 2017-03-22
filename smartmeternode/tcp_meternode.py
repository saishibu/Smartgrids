

#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-
import json
import socket               # Import socket module
def send(c_data):
	b=b''
#c_data=dict()
	s = socket.socket()         # Create a socket object
	host = '172.20.4.132' # Get local machine name
	port = 123    # Reserve a port for your service.
	
	#c_data={'name':'thank','age':30}
	#c_data_json=json.dumps(c_data)
	
	s.connect((host, port))
	s.sendall(c_data)
	#temp =s.recv(1024)
	#b +=temp
#d= json.loads(temp.encode('utf-8'))
	#print d
	
	s.close                     # Close the socket when done

