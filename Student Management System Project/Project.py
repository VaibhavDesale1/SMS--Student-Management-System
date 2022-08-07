# Student Management System Project in Python

from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
import bs4
import tkinter
list_marks = []
list_names = []

splash = Tk()
splash.after(2000, splash.destroy)
splash.wm_attributes('-fullscreen', 'true')
msg = Label(splash, text="Student \nManagement System \nby \nVaibhav Desale \n:-)", font=('Calibri', 100, 'bold'), fg='red')
msg.pack()
splash.mainloop()

def f1():
	add_window.deiconify()
	main_window.withdraw()

def f2():
	main_window.deiconify()
	add_window.withdraw()

def f3():
	view_window.deiconify()
	main_window.withdraw()
	view_window_st_data.delete(1.0, END)
	info = ""
	con = None
	try:
		con = connect('kc.db')
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + " rno = " + str(d[0])+ "\n name = " + str(d[1])+ "\n marks = " + str(d[2])+ "\n" + '*' * 40 + "\n"
		view_window_st_data.insert(INSERT, info)
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()

def f4():
	main_window.deiconify()
	view_window.withdraw()


def f5():
	con = None
	try:
		if (int(add_window_ent_marks.get()) < 0 or int(add_window_ent_marks.get()) > 100):
			showerror("Error ", 'Marks should be positive and less than 101' )
			add_window_ent_rno.focus()
			add_window_ent_marks.delete(0, END)

		elif (len(add_window_ent_name.get()) < 2) or (not add_window_ent_name.get().isalpha()): 
			showerror("Error ", 'Alphabets only' )
		elif int(add_window_ent_rno.get()) < 0 :
			showerror('Error', 'Rno should be positive \nEnter a valid Rno')
	
		else:
			try:
				con = connect('kc.db')
				cursor = con.cursor()
				sql = "insert into student values('%d', '%s', '%d')"
				rno = int(add_window_ent_rno.get())
				name = add_window_ent_name.get()
				marks = int(add_window_ent_marks.get())
				cursor.execute(sql % (rno, name, marks))
				con.commit()
				showinfo('Success', 'record added')
				add_window_ent_rno.focus()
				add_window_ent_rno.delete(0, END)
				add_window_ent_name.delete(0, END)
				add_window_ent_marks.delete(0, END)
			except Exception as e:
				showerror('Failure', e)
			except ValueError:
				showerror("Error", "Positive numbers only")
			finally:
				if con is not None:
					con.close()
	except ValueError:
			showerror("Error", "Rno should be positive and valid.\nYou have to enter Integers only\n\nFor Name,You have to enter Alphabets only\n\nFor Marks you have to enter Integers only")

def f6():
	try:
		wa = "https://www.brainyquote.com/quote_of_the_day"
		res = requests.get(wa)
		data = bs4.BeautifulSoup(res.text, 'html.parser')
		info = data.find('img', {'class':'p-qotd'})
		msg = info['alt']
		showinfo("The Quote of the day is ", str(msg))
	except Exception as e:
		showerror("issue ", e)


def f7():
	update_window.deiconify()
	main_window.withdraw()

def f8():
	delete_window.deiconify()
	main_window.withdraw()

def f9():
	con = None
	try:
		if int(update_window_ent_marks.get()) < 0 or int(update_window_ent_marks.get()) > 100:
			showerror("Error ", 'Marks should be positive and less than 100' )
			update_window_ent_rno.focus()
			update_window_ent_marks.delete(0, END)
		elif (len(update_window_ent_name.get()) < 2) or (not update_window_ent_name.get().isalpha()): 
			showerror("Error ", 'For Name, Enter Alphabets only and size should be greater than 1' )
		elif int(update_window_ent_rno.get()) < 0 :
			showerror('Error', 'Rno should be positive \nEnter a valid Rno')

		else:
			try:
				con = connect("kc.db")
				cursor = con.cursor()
				sql  = "update student set name='%s', marks='%d' where rno='%d' "
				rno = int(update_window_ent_rno.get())
				name = update_window_ent_name.get()
				marks = int(update_window_ent_marks.get())
				cursor.execute(sql % (name, marks, rno))
				if cursor.rowcount > 0: 
					showinfo('Success', 'record updated')
					con.commit()
				else:
					showerror('Success', 'record does not exists')
				update_window_ent_rno.focus()
				update_window_ent_rno.delete(0, END)
				update_window_ent_name.delete(0, END)
				update_window_ent_marks.delete(0, END)

			except Exception as e:
				showerror('Failure', e)
			except ValueError:
				showerror("Error", "Positive numbers only")
				update_window_ent_rno.focus()
				update_window_ent_rno.delete(0, END)
			finally:
				if con is not None:
					con.close()
	except ValueError:
			showerror("Error", "Rno should be positive and valid.\nYou have to enter Integers only\n\nFor Name,You have to enter Alphabets only\n\nFor Marks you have to enter Integers only")
			update_window_ent_rno.focus()
			update_window_ent_rno.delete(0, END)

def f10():
	con = None
	try:
		if int(delete_window_ent_rno.get()) < 0 :
			showerror('Error', 'Rno should be positive \nEnter a valid Rno')
		else:
			try:
				con = connect("kc.db")
				cursor = con.cursor()
				sql  = "delete from student where rno='%d' "
				delete_window_ent_rno.focus()
				rno = int(delete_window_ent_rno.get())
				cursor.execute(sql % (rno))
				if cursor.rowcount > 0:
					showinfo('Success', 'record deleted')
					con.commit()
					delete_window_ent_rno.focus()
					delete_window_ent_rno.delete(0, END)
				else:
					showerror('Success', 'record does not exists')
					delete_window_ent_rno.focus()
					delete_window_ent_rno.delete(0, END)	

			except Exception as e:
				showerror('Failure', e)
			except ValueError:
				showerror("Error", "Positive numbers only")
			finally:
				if con is not None:
					con.close()
	except ValueError:
			showerror("Error", "Number should be positive and valid.\nYou have to enter Integers only")
			delete_window_ent_rno.focus()
			delete_window_ent_rno.delete(0, END)	
def f11():
	con=None
	try:
		con=connect('kc.db')
		cursor=con.cursor()
		sql="select marks from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:	
			list_marks.append(int(str(d[0])))
		
	except Exception as e:
		print(e)
	finally:
		if con is not None:
			con.close()

	try:
		con=connect('kc.db')
		cursor=con.cursor()
		sql="select name from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:	
			list_names.append(str(d[0]))
		
	except Exception as e:
		print(e)
	finally:
		if con is not None:
			con.close()

	plt.bar(list_names, list_marks, width = 0.6, color = ['red', 'green', 'blue', 'red', 'green'])
	plt.title("Analysis")
	plt.xlabel("Students")
	plt.ylabel("Marks")
	plt.show()

def f12():
	main_window.deiconify()
	update_window.withdraw()

def f13():
	main_window.deiconify()
	delete_window.withdraw()

def f14():
	try:
		city_name = temp_window_ent_city_name.get()
		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + city_name
		a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
		wa = a1 + a2 + a3
		res = requests.get(wa)
		data = res.json()
		main = data['main']
		temp = main['temp']
		msg = str(temp) + " \u2103 "
		showinfo("Temp", msg)
	except Exception as e:
		print("issue ", e)

def f15():
	temp_window.deiconify()
	main_window.withdraw()

def f16():
	main_window.deiconify()
	temp_window.withdraw()

def f17():
	try:
		wa = "https://ipinfo.io/"
		res = requests.get(wa)
		data = res.json()
		city_name = data['city']
		state_name = data['region']
		loc= data['loc']

		info = loc.split(",")
		msg = "City = " + city_name + "\nState = " + state_name + "\nLat = " + info[0] + "\nLong = " + info[1]		
		showinfo("LOCATION", msg)

	except Exception as e:
		showerror("issue ", e)

main_window = Tk()
main_window.title("S. M. S.")
main_window.geometry("550x550+400+100")

main_window_btn_add = Button(main_window, text="Add", font=('Arial', 20, 'bold'), width=10, command=f1)
main_window_btn_view = Button(main_window, text="View", font=('Arial', 20, 'bold'), width=10, command=f3)
main_window_btn_update = Button(main_window, text="Update", font=('Arial', 20, 'bold'), width=10, command=f7)
main_window_btn_delete = Button(main_window, text="Delete", font=('Arial', 20, 'bold'), width=10, command=f8)
main_window_btn_charts = Button(main_window, text="Charts", font=('Arial', 20, 'bold'), width=10, command=f11)

main_window_btn_location = Button(main_window, text="LOCATION:", bd=5, font=('Arial', 20, 'bold'), command=f17)
main_window_btn_temp = Button(main_window, text="TEMP:", bd=5,  font=('Arial', 20, 'bold'), width=10, command=f15)
main_window_btn_qotd = Button(main_window, text="QOTD:", bd=5,  font=('Arial', 20, 'bold'), width=10, command=f6)

main_window_btn_add.pack(pady=10)
main_window_btn_view.pack(pady=10)
main_window_btn_update.pack(pady=10)
main_window_btn_delete.pack(pady=10)
main_window_btn_charts.pack(pady=10)

main_window_btn_location.pack(side='left', padx=10)
main_window_btn_temp.pack(side='right', padx=10)
main_window_btn_qotd.pack(side='bottom', pady=10)

add_window = Toplevel(main_window)
add_window.title("Add St.")
add_window.geometry("500x500+400+100")
 
add_window_lbl_rno = Label(add_window, text="enter rno", font=('Arial', 20, 'bold'))
add_window_ent_rno = Entry(add_window, bd=5, font=('Arial', 20, 'bold'))
add_window_lbl_name = Label(add_window, text="enter name", font=('Arial', 20, 'bold'))
add_window_ent_name = Entry(add_window, bd=5, font=('Arial', 20, 'bold'))
add_window_lbl_marks = Label(add_window, text="enter marks", font=('Arial', 20, 'bold'))
add_window_ent_marks = Entry(add_window, bd=5, font=('Arial', 20, 'bold'))
add_window_btn_save = Button(add_window, text="Save", font=('Arial', 20, 'bold'), command=f5)
add_window_btn_back = Button(add_window, text="Back", font=('Arial', 20, 'bold'), command=f2)

add_window_lbl_rno.pack(pady=10)
add_window_ent_rno.pack(pady=10)
add_window_lbl_name.pack(pady=10)
add_window_ent_name.pack(pady=10)
add_window_lbl_marks.pack(pady=10)
add_window_ent_marks.pack(pady=10)
add_window_btn_save.pack(pady=10)
add_window_btn_back.pack(pady=10)
add_window.withdraw()

view_window = Toplevel(main_window)
view_window.title("View St.")
view_window.geometry("500x500+400+100")

view_window_st_data = ScrolledText(view_window, width=40, height=10, font=('Arial', 20, 'bold'))
view_window_btn_back = Button(view_window, text="Back", font=('Arial', 20, 'bold'), command=f4)
view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)
view_window.withdraw()

# --> update window
update_window = Toplevel(main_window)
update_window.title("Update St.")
update_window.geometry("500x500+400+100")

update_window_lbl_rno = Label(update_window, text="enter rno", font=('Arial', 20, 'bold'))
update_window_ent_rno = Entry(update_window, bd=5, font=('Arial', 20, 'bold'))
update_window_lbl_name = Label(update_window, text="enter name", font=('Arial', 20, 'bold'))
update_window_ent_name = Entry(update_window, bd=5, font=('Arial', 20, 'bold'))
update_window_lbl_marks = Label(update_window, text="enter marks", font=('Arial', 20, 'bold'))
update_window_ent_marks = Entry(update_window, bd=5, font=('Arial', 20, 'bold'))
update_window_btn_save = Button(update_window, text="Save", font=('Arial', 20, 'bold'), command=f9)
update_window_btn_back = Button(update_window, text="Back", font=('Arial', 20, 'bold'), command=f12)

update_window_lbl_rno.pack(pady=10)
update_window_ent_rno.pack(pady=10)
update_window_lbl_name.pack(pady=10)
update_window_ent_name.pack(pady=10)
update_window_lbl_marks.pack(pady=10)
update_window_ent_marks.pack(pady=10)
update_window_btn_save.pack(pady=10)
update_window_btn_back.pack(pady=10)
update_window.withdraw()

# --> delete window
delete_window = Toplevel(main_window)
delete_window.title("Delete St.")
delete_window.geometry("500x500+400+100")

delete_window_lbl_rno = Label(delete_window, text="enter rno", font=('Arial', 20, 'bold'))
delete_window_ent_rno = Entry(delete_window, bd=5, font=('Arial', 20, 'bold'))
delete_window_btn_save = Button(delete_window, text="Save", font=('Arial', 20, 'bold'), command=f10)
delete_window_btn_back = Button(delete_window, text="Back", font=('Arial', 20, 'bold'), command=f13)
delete_window_lbl_rno.pack(pady=10)
delete_window_ent_rno.pack(pady=10)
delete_window_btn_save.pack(pady=10)
delete_window_btn_back.pack(pady=10)
delete_window.withdraw()


# Temp Window

temp_window = Toplevel(main_window)
temp_window.title("Temperature :)  ")
temp_window.geometry("500x500+400+100")

temp_window_lbl_city_name = Label(temp_window, text="enter city name", font=('calibri', 18, 'bold'))
temp_window_ent_city_name = Entry(temp_window, bd = 4, font=('calibri', 18, 'bold'))
temp_window_btn_find = Button(temp_window, text="Find", font=('calibri', 18, 'bold'), command=f14)
temp_window_btn_back = Button(temp_window, text="Back", font=('calibri', 18, 'bold'), command=f16)

temp_window_lbl_city_name.pack(pady=20)
temp_window_ent_city_name.pack(pady=20)
temp_window_btn_find.pack(pady=20)
temp_window_btn_back.pack(pady=20)
temp_window_ent_city_name.focus()
temp_window.withdraw()


main_window.mainloop()
