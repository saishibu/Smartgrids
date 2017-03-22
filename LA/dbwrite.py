import time
import psycopg2

def todb (data):
    
    conn =psycopg2.connect(database="la",user="postgres",password="amma",host="localhost",port="5432")
    print("DB Open Successful\n")
    cur=conn.cursor()
    cur.execute("""INSERT INTO latable(time,meter,temperature,frequency,penergy,qenergy,senergy,cospi,irms,vrms,ppower,qpower,spower,event) VALUES (%(time)s, %(meter)s, %(temperature)s, %(freq)s, %(penergy)s, %(qenergy)s, %(senergy)s, %(cospi)s, %(irms)s, %(vrms)s, %(ppower)s, %(qpower)s, %(spower)s, %(event)s); """, data)	
    conn.commit()
    conn.close()
