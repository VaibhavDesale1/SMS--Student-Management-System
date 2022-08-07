# inserting record in table (insert static data) --> data will be decided by the programmer

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / opened ")
	cursor = con.cursor()
	sql = "insert into student values(10, 'sumit', 60)"
	cursor.execute(sql)
	print("record created")
	con.commit()		# database me save krna 
except Exception as e:
	print("issue ", e)
	con.rollback()		# save nahi krna / nahi kiya to bhi chalta hai
finally:
	if con is not None:
		con.close()
		print("closed")