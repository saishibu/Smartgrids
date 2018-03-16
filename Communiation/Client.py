import serial
import time
import socket
TCP_IP = '192.168.1.6'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World2!"
Zigbee_count=0
Wifi_count=0
loop1_count=0
Zigbee1_count=0
loop_count=0
power_initial=0
main_count=0

def Zigbee():
    ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5)
    ser.write('Hello user2\r\n')
    time.sleep(.01)
    incoming = ser.readline().strip()
    print ("Received Data : "+ incoming )
    ser.close()
    return incoming

def initialization():
    ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5)
    time.sleep(1)
    ser.write('+++')
    time.sleep(1)
    incoming = ser.readline().strip()
    print ("Received Data : "+ incoming )
    ser.write('ATPL = 2\r\n')
    incoming = ser.readline().strip()
    print ("Received Data : "+ incoming )
    ser.write('ATPL\r\n')
    incoming = ser.readline().strip()
    print ("Current Power level : "+ incoming )
    ser.write('ATCN\r\n')
    ser.close()
    power_initial = 1
    return power_initial

def Transmitted_power(main_count,Zigbee_count,loop_count):
    while Zigbee_count < 1:
        incoming = Zigbee()
        if not incoming:
            loop_count= loop_count+1
            if loop_count == 15:
                Zigbee_count = 2
                Wifi_count = 0 
	elif incoming == "OK":
            Zigbee_count=0
            loop_count =0
    while Zigbee_count == 2:
        ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5)
        print "Check the Power Level"
        time.sleep(1)
        ser.write('+++')
        time.sleep(1)
        incoming = ser.readline().strip()
        print ("Received Data : "+ incoming )
        ser.write('ATPL\r\n')
        incoming = ser.readline().strip()
        print ("Current Power level : "+ incoming )
        if incoming == '2':
            print "Change the Power Level"
            ser.write('ATPL = 3\r\n')
            loop_count=0
            Zigbee_count =0
            main_count =0
        if incoming == '3':
            print "Change the Power Level"
            ser.write('ATPL = 4\r\n')
            loop_count=0
            Zigbee_count =0
            main_count=0
        if incoming == '4':
            main_count = 2
            Zigbee_count = 5
        time.sleep(1)
        ser.write('ATCN\r\n')
        ser.close()
    return main_count

def Wifi():
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    print "received data:", data
    return

    
while True:
    if power_initial == 0:
        power_initial=initialization()
    while main_count < 1:
        main_count = Transmitted_power(main_count,Zigbee_count,loop_count)
    while main_count > 1:
        while Zigbee1_count < 1:
            incoming = Zigbee()
            if not incoming:
                loop1_count= loop1_count+1
               # print "loop1_count:",loop1_count
                if loop1_count == 5:
                    Zigbee1_count = 2
            elif incoming == "OK":
                Zigbee1_count=0
                loop1_count =0
        while Zigbee1_count > 1:
            print "Switched to WiFi"
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            while Wifi_count < 15:
                Wifi()
                Wifi_count = Wifi_count+1
            s.close()
            Zigbee1_count=0
            loop1_count = 0
            print "Switched to Zigbee"
    
 
