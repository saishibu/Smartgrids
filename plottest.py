import math
f=open('mydata.dat','w')

for degrees in range(720):
	si=math.sin(math.radians(degrees))
	co=0.5*math.cos(math.radians(degrees))
	if si>0:
		sq=0.6
	else:
		sq=-0.6

	data ="{}{}{}\n".format(degrees,si,co,sq)
	f.write(data)
f.close()
