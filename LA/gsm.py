import serial
import RPi.GPIO as GPIO
import os
from time import sleep

GPIO.setmode(GPIO.BOARD)

gsm=serial.Serial("/dev/ttyS0",baudrate=9600,timeout=1)

gsm.write('AT\r')
rcv=port.read(10)
print rcv


