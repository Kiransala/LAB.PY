from tkinter import *
import sqlite3

with sqlite3.connect("detail.db") as db:
	cursor = db.cursor()
	
cursor.execute("Create table if not exists users(username text primary key); ")


def add_user():
	user= username.get()
	
	cursor.execute("select count(*) from users where username='"+user+"'")
	result= cursor.fetchone()
	
	if  int(result[0])>0:
		error["text"]="username already exists"
	else:
		error["text"]="user added"
		cursor.execute("insert into users(username) values('"+user+"')")
		db.commit()
		

	
window = Tk()
window.geometry("450x120")

error = Message(text="" , width=160)
error.place(x=30,y=10)

label1=Label(text="Username")
label1.place(x=30,y=40)

username = Entry(text="")
username.place(x=150,y=40,width=200, height=25)

button = Button(text="Add", command= add_user)
button.place(x=150,y=80,width=75,height=35)

window.mainloop()
