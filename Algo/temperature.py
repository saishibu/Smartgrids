#Algorithm for Temperature error check
#Code by Nikhitha
#Temperature error considered as 'low priority' error. LED gives warning in case of any errors
#this algorithm is implemented in the Load meter main program
    
from gpiozero import LED
from time import sleep
def temperature(t):
    if(t>29.5 and t<30 or t>30 and t<30.5): # when the temperature in the range of 29.5 and 30 or 30 and 30.5
        led=LED(17)#GPIO 17th pin #LED colour GREEN
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()
    elif(t<29.5 or t>30.5):
        led=LED(21)#GPIO 21st pin #LED colour RED
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()
    else: # in the condition when "temperature" t==30
        led=LED(13)#GPIO 13th pin #LED colour YELLOW
        led.on()
        sleep(2)# time delay of 2 secs
        led.off()
            
