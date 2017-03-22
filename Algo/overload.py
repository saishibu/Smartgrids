#Algorithm for Overload error check
#Code by Nikhitha
#Overload error considered as 'medium priority' error. LED gives warning in case of any errors
#this algorithm is implemented in the Load meter main program
    
from gpiozero import LED
from time import sleep
def current(c):
    if(c>9 and c<10 or c>10 and c<11):# when the current in the range of 9 and 10 or 10 and 11
        led=LED(17)#GPIO 17th pin #LED colour GREEN
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()
    elif(c<10 or c>11):
        led=LED(21)#GPIO 21st pin #LED colour RED
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()
        led=LED(20)#GPIO 20th pin for alarm
        sleep(1) # time delay of 2 secs
        led.off()
    else: # in the condition when "current" c==10
        led=LED(13)#GPIO 13th pin #LED colour YELLOW
        led.on()
        sleep(2)# time delay of 2 secs
        led.off()
            



















from gpiozero import LED
from time import sleep
def current(c):
    if(c>9.5 and c<10):
        led=LED(14)
        led.on()
        sleep(2)
        led.off()
    elif(c>10 and c<10.5):
        led=LED(14)
        led.on()
        sleep(2)
        led.off()
    else:
        led=LED(14)
        led.off()
        sleep(10)
