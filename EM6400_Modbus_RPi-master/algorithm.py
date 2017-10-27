def theft(t):
	import pymysql
	conn_IN = pymysql.connect(database="INTELLIGENTNODE", user="root",password= "root", host="192.168.1.14")
#conn_local = pymysql.connect(database="INTELLIGENTNODE", user="root",password= "root", host="localhost")
	print "Opened database successfully"
	cur_IN = conn_IN.cursor()
	cur_IN.execute("SELECT irms from nodedata ORDER BY ID DESC limit 1;")
	data=cur_IN.fetchone()
	conn_IN.close()
	print data
	if (t != data[0]):
		return 1
	else:
		return 0
