# Charts
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlite3 import *

info = ""
con = None
try:
	con = connect('kc.db')
	cursor = con.cursor()
	sql = "select * from student"
	cursor.execute(sql)
	data = cursor.fetchall()
	for d in data:
		info = info + "\n name = " + str(d[1])+ "\n marks = " + str(d[2])
		print(info)
except Exception as e:
	print('Failure', e)
finally:
	if con is not None:
		con.close()
"""
	name = []
	marks = []
	plt.plot(name, marks, linewidth=4)
	plt.xlabel("Names of Students")
	plt.ylabel("Marks")
	plt.title("Batch Information")
	plt.show()


language = data['LANGUAGE'].tolist()
Jobs_2017= data['JOBS_2017'].tolist()
Jobs_2018= data['JOBS_2018'].tolist()

x = np.arange(len(language))
plt.bar(x, Jobs_2017, width=0.25, label='2017')
plt.bar(x + 0.25, Jobs_2018, width=0.25, label='2018')
plt.xticks(x, language)

plt.xlabel("Languages")
plt.ylabel("Jobs")
plt.title("Job Demand")

plt.grid()
plt.legend()
plt.show()

"""
