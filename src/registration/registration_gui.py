from tkinter import Label,Frame, Entry, Button, StringVar
import tkinter as tk
from main import *
import db_connection
import time

def registration_frame(parent,show_frame):
    registration_frame=Frame(parent,bg="#f0fff0")
    global password
    global username

    Label(registration_frame, text="Register Your Account", font=("Helvetica", 12), bg="#f0fff0", fg="dark green", width=300).pack()
    username = StringVar()
    password = StringVar()

    Label(registration_frame,bg="#f0fff0").pack()
    Label(registration_frame, text="Username : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Entry(registration_frame, textvariable=username).pack()
    Label(registration_frame,bg="#f0fff0").pack()
    Label(registration_frame, text="Password : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Entry(registration_frame, textvariable=password, show="*").pack()
    Button(registration_frame, text="Register", font=("Helvetica", 12), bg="light green", fg="dark green", command=register_user).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    if username_info == "" or password_info == "":
        error()
    else:
        sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
        t = (username_info, password_info)
        db_connection.mycursor.execute(sql, t)
        db_connection.mydb.commit()
        Label(registration_frame,bg="#f0fff0").pack()
        time.sleep(1)
        success()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    registration_frame.destroy()

def error():
    global err
    err=Frame(parent=registration_frame,bg="#f0fff0")
    Label(err, text="All fields are required...", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Label(err,bg="#f0fff0").pack()
    Button(err, text="OK", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=error_destroy).pack()

def success():
    global succ
    succ=Frame(parent=registration_frame,bg="#f0fff0")
    Label(succ, text="Registration successful...", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Label(succ,bg="#f0fff0").pack()
    Button(succ, text="OK", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=succ_destroy).pack()
