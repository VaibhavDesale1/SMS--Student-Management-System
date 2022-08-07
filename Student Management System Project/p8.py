# delete

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / opened ")
	cursor = con.cursor()
	sql  = "delete from student where rno='%d' "
	rno = int(input("enter rno to be deleted "))
	cursor.execute(sql % (rno))
	print(cursor.rowcount)
	if cursor.rowcount > 0:
		print("record deleted")
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