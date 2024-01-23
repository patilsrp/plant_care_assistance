from tkinter import Label,Frame, Entry, Button, StringVar
import tkinter as tk
from main import *
import db_connection

def login_frame(parent,show_frame):
    login_frame=Frame(parent,bg="#f0fff0")
    global username_verify
    global password_verify
    Label(login_frame, text="Login", font=("Helvetica", 12), bg="#f0fff0", fg="dark green", width=300).pack()
    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_frame,bg="#f0fff0").pack()
    Label(login_frame, text="Username : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Entry(login_frame, textvariable=username_verify).pack()

    Label(login_frame,bg="#f0fff0").pack()
    Label(login_frame, text="Password : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Entry(login_frame, textvariable=password_verify, show="*").pack()
    Button(login_frame, text="Log-In", font=("Helvetica", 12), bg="light green", fg="dark green", command=login_verify).pack()
    Label(login_frame,bg="#f0fff0").pack()
    return login_frame

def login_verify():
    user_verify = username_verify.get()
    pass_verify = password_verify.get()
    sql = "SELECT * FROM login WHERE username = %s AND password = %s"
    db_connection.mycursor.execute(sql, [(user_verify), (pass_verify)])
    results = db_connection.mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def logged():
    global logg
    logg = Frame(root)
    logg.grid(row=0,column=0,sticky="nsew") 

    Label(logg, text="Welcome {}".format(username_verify.get()), fg="green",bg="#f0fff0", font="bold").pack()
    Label(logg,bg="#f0fff0").pack()
    Button(logg, text="Browse", height=1, font=("Helvetica", 12), bg="light green", fg="dark green", width=15).pack()
    Button(logg, text="Log-out", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=login_destroy).pack()
    
def failed():
    global fail 
    fail =Frame(root)
    fail.grid(row=0,column=0,sticky="nsew") 
    
    Label(fail, text="Invalid Credentials...", font=("Helvetica", 12), bg="light green", fg="dark green").pack()
    Label(fail, bg="light green").pack()
    Button(fail, text="OK", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=fail_destroy).pack()

def fail_destroy():
    fail.destroy()

def login_destroy():
    logg.destroy()
    login_page.destroy()