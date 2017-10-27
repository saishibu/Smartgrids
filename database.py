import pymysql

conn=pymysql.connect(database='INTELLIGENTNODE', user='root',password='root',host='192.168.1.14')

print "Opened database successfully"

cur = conn.cursor()

