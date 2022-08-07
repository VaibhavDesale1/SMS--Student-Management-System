# view record (select) --> fetchall() --> ek saath record

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / open ")
	cursor = con.cursor()
	sql = "select * from student"
	cursor.execute(sql)
	data = cursor.fetchall()	# list of tuples 		[(rno,name, marks) (...) () ]
	print(data)
	
	for d in data:
		print("rno = ", d[0], 'name = ', d[1], 'marks = ', d[2])

except Exception as e:
	print("issue ", e)
	
finally:
	if con is not None:
		con.close()
		print("closed")