
def frequency(f):
	if(f>=49 and f<50):
		return 1
	elif(f>50 and f<=51):
		return 2
	elif(f<49 or f>51):	
        	return 3
	else:
		return 0
#	freq = frequency(f)
#	print(freq)
def voltage(v):
	if(v>=229 and v<230):
                return 1
        elif(v>230 and v<=231):
                return 2
        elif(v<229 or v>231):
                return 3
        else:
                return 0
def temperature(t):
	if(t>=29 and t<30):
                return 1
        elif(t>30 and t<=31):
                return 2
        elif(t<29 or t>31):
                return 3
        else:
                return 0
def overload(o):
	if(o>=100 and o<105):
		return 1
	elif(o>=105): 
		return 2
	else:
		return 0
def linebreakage(f,v):
	if(f==0 or v==0): 
		return 1
	else:
		return 0
    	            

#def eventdb():

