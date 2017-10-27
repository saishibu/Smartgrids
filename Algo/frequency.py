#Algorithm for Frequency error check
#Code by Nikhitha
#Frequency deviation considered as 'low priority' error. LED gives warning in case of any errors
#This program also gives alarm in case of critical condition
#this algorithm is implemented in the Load meter main program
    
#from gpiozero import LED
#from time import sleep
def frequency(f):
    if(f>=49 and f<50 or f>50 and f<=51 or f<49 or f>51): # when the frequency in the range of 49.5 and 50 or 50 and 50.5
        return "1"#GPIO 17th pin #LED colour GREEN
       # led.on()
       # sleep(2) # time delay of 2 secs
       # led.off()
       # print"1"#GPIO 21st pin #LED colour RED
       # led.on()
       # sleep(2) # time delay of 2 secs
       # led.off()
       # led=LED(20)#GPIO 20th pin for alarm
       # sleep(1) # time delay of 2 secs
       # led.off()
    else: # in the condition when "frequency" f==50
        return"0"#GPIO 13th pin #LED colour YELLOW
       # led.on()
       # sleep(2) # time delay of 2 secs
       # led.off()
    	            
       
