# create database

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / open ")
except Exception as e:
	print("issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")