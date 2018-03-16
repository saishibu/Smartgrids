import pymysql
import random
from random import randint

conn = pymysql.connect(db="CS", user="root", password="root", host="localhost")
print "Opened database successfully"
cur= conn.cursor()

Meter=1
V=randint(0, 9)
I=randint(0, 9)
temp=randint(0, 9)
P_pwr=randint(0, 9)
Q_pwr=randint(0, 9)
S_pwr=randint(0, 9)
P_eng=randint(0, 9)
Q_eng=randint(0, 9)
S_eng=randint(0, 9)
pf=randint(0, 9)
f=randint(0, 9)

data={'Meter':Meter,'V':V,'I':I,'temp':temp,'P_pwr':P_pwr,'Q_pwr':Q_pwr,'S_pwr':S_pwr,'P_eng':P_eng,'Q_eng':Q_eng,'S_eng':S_eng,'f':f,'pf':pf}
print data

cur.execute("INSERT INTO IN1(Meter,V,I,temp,Ppwr,Qpwr,Spwr,Peng,Qeng,Seng,f,pf) VALUES(%(Meter)s,%(V)s,%(I)s,%(temp)s,%(P_pwr)s,%(Q_pwr)s,%(S_pwr)s,%(P_eng)s,%(Q_eng)s,%(S_eng)s,%(f)s,%(pf)s);",data)
conn.commit()
print "DB Updated"
conn.close()


