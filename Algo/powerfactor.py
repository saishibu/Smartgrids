#Algorithm for Powerfactor check
#Code by Nikhitha
#This program is used to check whether the Powerfactor is in lagging or unity condition
#this algorithm is implemented in the Load meter main program
    
from gpiozero import LED
from time import sleep
def powerfactor(pf):
    if(pf==1): # unity powerfactor with good load
        led=LED(17)#GPIO 17th pin #LED colour GREEN
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()
    elif(pf<1 and pf>0.85): #lagging powerfactor with good load
        led=LED(21)#GPIO 21st pin #LED colour RED
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()

