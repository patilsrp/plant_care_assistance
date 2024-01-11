from tkinter import Label,Frame, Entry, Button, StringVar
import tkinter as tk
from main import *
import db_connection

def login():
    global login_page
    login_page.tkraise()
    login_page= Frame(root)
    login_page.grid(row=0,column=0) 
    login_page.configure(bg="#f0fff0")
    global username_verify
    global password_verify
    Label(login_page, text="Login", font=("Helvetica", 12), bg="#f0fff0", fg="dark green", width=300).pack()
    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_page,bg="#f0fff0").pack()
    Label(login_page, text="Username : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Entry(login_page, textvariable=username_verify).pack()

    Label(login_page,bg="#f0fff0").pack()
    Label(login_page, text="Password : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Entry(login_page, textvariable=password_verify, show="*").pack()
    Button(login_page, text="Log-In", font=("Helvetica", 12), bg="light green", fg="dark green", command=login_verify).pack()
    Label(login_page,bg="#f0fff0").pack()
    

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
    logg.grid() 
    logg.configure(bg="#f0fff0")
    Label(logg, text="Welcome {}".format(username_verify.get()), fg="green", bg="#f0fff0", font="bold").grid(row=0, column=0, columnspan=2)
    Label(logg, bg="#f0fff0").grid(row=1, column=0)
    Button(logg, text="Browse", height=1, font=("Helvetica", 12), bg="light green", fg="dark green", width=15).grid(row=2, column=0, columnspan=2, pady=5)
    Button(logg, text="Log-out", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=login_destroy).grid(row=3, column=0, columnspan=2, pady=5)

def failed():
    global fail 
    fail =Frame(root)
    fail.grid(row=0,column=0) 
    tk.Label(fail,text="Login").grid(row=0)
    fail.configure(bg="#f0fff0")
    #Label(fail, text="Invalid Credentials...", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").grid(row=0, column=0, columnspan=2)
    #Label(fail, bg="#f0fff0").grid(row=1, column=0)
    #Button(fail, text="OK", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=fail_destroy).grid(row=2, column=0, columnspan=2, pady=5)

    Label(fail, text="Invalid Credentials...", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Label(fail, bg="#f0fff0").pack()
    Button(fail, text="OK", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=fail_destroy).pack()

def fail_destroy():
    fail.destroy()

def login_destroy():
    logg.destroy()
    login_page.destroy()

