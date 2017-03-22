#Algorithm for Line breakage check
#Code by Nikhitha
#Line breakage error is considered as 'high priority' error. LED gives warning and alaram indication in case of any errors a
#this algorithm is implemented in the grid meter main program
    
from gpiozero import LED
from time import sleep
def Line breakage(l):
        led=LED(17)#GPIO 17th pin #LED colour GREEN
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()
        led=LED(20)#GPIO 20th pin for alarm
        sleep(1) # time delay of 2 secs
        led.off()

# the  following condition for line breakage is written in main program
#if(realpower==0):











    
