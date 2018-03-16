import time
import pymysql

def todb (node_data):
    
	conn =pymysql.connect(database="IN",user="on",password="amma",host="localhost")
	print("DB Open Successful\n")
	cur=conn.cursor()
	cur.execute("INSERT INTO IN1(Meter,V,I,temp,Ppwr,Qpwr,Spwr,Peng,Qeng,Seng,f,pf) VALUES(%(Meter)s,%(V)s,%(I)s,%(temp)s,%(P_pwr)s,%(Q_pwr)s,%(S_pwr)s,%(P_eng)s,%(Q_eng)s,%(S_eng)s,%(f)s,%(pf)s);",node_data)
	conn.commit()
	conn.close()
	print "Data Updated to DB"
