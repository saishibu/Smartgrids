#Algorithm for Voltage error check
#Code by Nikhitha
#voltage error considered as 'low priority' error. LED gives warning in case of any errors
#This program also gives alarm in case of critical condition
#this algorithm can be implemented in both Load meter and Grid meter main programs
#voltage error checked in the program is of single phase i.e. 230V


from gpiozero import LED
from time import sleep
def voltage(v):
    if(v>229 and v<230 or v>230 and v<231): # when the voltage in the range of 229 and 230 or 230 and 231
        led=LED(17)#GPIO 17th pin #LED colour GREEN
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()
    elif(v<229or v>231):
        led=LED(21)#GPIO 21st pin #LED colour RED
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()
        led=LED(20)#GPIO 20th pin for alarm
        sleep(1) # time delay of 2 secs
        led.off()
    else: # in the condition when "voltage" v==230
        led=LED(13)#GPIO 13th pin #LED colour YELLOW
        led.on()
        sleep(2) # time delay of 2 secs
        led.off()
            













