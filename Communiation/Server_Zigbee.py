import serial
import socket
TCP_IP = '192.168.1.106'
TCP_PORT = 5005
BUFFER_SIZE = 20
# Enable USB Communication
zig_count=0
zig_not_count=0
wifi_send_count=0
loop_count=0
while True:
    while (zig_count == 0):
        ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5)
        incoming = ser.readline().strip()
        print 'Received Data : '+ incoming
        if not incoming :
            loop_count=loop_count+1
        else:
            ser.write('OK \r\n')
            zig_count=0
            loop_count=0

        
        


