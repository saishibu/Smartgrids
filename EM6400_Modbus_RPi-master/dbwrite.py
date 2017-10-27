import time
import pymysql

def todb (data):
    
    conn =pymysql.connect(database="SGL",user="root",password="root",host="localhost")
    print("DB Open Successful\n")
    cur=conn.cursor()
    cur.execute("""INSERT INTO 3phSource(meter,temperature,freq,penergy,qenergy,senergy,cospi,irms,vrms,ppower,qpower,spower,event) VALUES (%(meter)s, %(temperature)s, %(freq)s, %(penergy)s, %(qenergy)s, %(senergy)s, %(cospi)s, %(irms)s, %(vrms)s, %(ppower)s, %(qpower)s, %(spower)s; """, data)	
    conn.commit()
    conn.close()
