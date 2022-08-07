# update

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / opened ")
	cursor = con.cursor()
	sql  = "update student set name='%s', marks='%d' where rno='%d' "
	rno = int(input("enter rno "))
	name = input("enter new name ")
	marks = int(input("enter new marks "))
	cursor.execute(sql % (name, marks, rno))
	if cursor.rowcount > 0: 
		print("record updated")
		con.commit()
	else:
		print("record does not exists ")

except Exception as e:
	print("issue ", e)
	con.rollback()	

finally:
	if con is not None:
		con.close()
		print("closed")