#Algorithm for Powertheft error check
#Code by Nikhitha
#Power theft error can be considered as 'High priority' error. LED gives warning in case of any errors
#This program also gives alarm in case of critical condition
#The program is for two cases
#The program is not yet completed

#Case1:a)The following program is used to check the Power theft that is happened between SCN( Smart consumer node)
#      b)This program is written in the Grid meter Rpi
#      c)m15_data is the current i.e "irms" value getting from grid meter(SDN)("reference value")
from gpiozero import LED
from time import sleep
c1= data['irms1']# current value recieved from LM1
c2= data['irms2']# current value recieved from LM2
c=c1+c2 # recieved value
if(m15_data-c<1 and m15_data!=c): # If the difference between recieved and reference value is less than "1" warning is given
    led=LED(21)#GPIO 21st pin #LED colour GREEN
    led.on()
    sleep(2) # time delay of 2 secs
    led.off()
elif(m15_data!=c):# there is power theft
    led=LED(17)#GPIO 17th pin #LED colour RED
    led.on()
    sleep(2) # time delay of 2 secs
    led.off()
else: # there is no power theft
    led=LED(13)#GPIO 13th pin #LED colour YELLOW
    led.on()
    sleep(2) # time delay of 2 secs
    led.off()
    
#Case2:a)The following program is used to check the Power theft that is happened between SDN( Smart distribution node)
#      b)This program is written in the Rpi of meter placed in STN( Smart transformer node)
#      c)m15_data is the current i.e "irms" value getting from meter placed in STN("reference value")
from gpiozero import LED
from time import sleep
c1= data['irms1']# current value recieved from GM1
c2= data['irms2']# current value recieved from GM2
c=c1+c2 # recieved value
if(m15_data-c<1 and m15_data!=c):# If the difference between recieved and reference value is less than "1" warning is given
    led=LED(21)#GPIO 21st pin #LED colour GREEN
    led.on()
    sleep(2) # time delay of 2 secs
    led.off()
elif(m15_data!=c): # there is power theft 
    led=LED(17)#GPIO 17th pin #LED colour RED
    led.on()
    sleep(2) # time delay of 2 secs
    led.off()
else: # there is no power theft
    led=LED(13)#GPIO 13th pin #LED colour YELLOW
    led.on()
    sleep(2) # time delay of 2 secs
    led.off()
    
    
    







