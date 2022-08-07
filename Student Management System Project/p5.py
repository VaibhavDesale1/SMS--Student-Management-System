# view record --> fetchone() --> ek ek krkr record

from sqlite3 import * 

con = None
try:
	con = connect("kc.db")
	print("database created / open ")
	cursor = con.cursor()
	sql = "select * from student"
	cursor.execute(sql)
	data = cursor.fetchone()
	while data:
		print(data)
		data = cursor.fetchone()
	
except Exception as e:
	print("issue ", e)
	
finally:
	if con is not None:
		con.close()
		print("closed")