import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
from main import root
import db_connection

def registration():
    global reg_page
    reg_page = tk.Frame(root)
    reg_page.grid()
    reg_page.configure(bg="#f0fff0")

    global password
    global username

    #Label(reg_page, text="Register Your Account", font=("Helvetica", 12), bg="#f0fff0", fg="dark green", width=300).grid(row=0, column=0, columnspan=2)
    username = StringVar()
    password = StringVar()

    #Label(reg_page, bg="#f0fff0").grid(row=1, column=0, pady=5)
    #Label(reg_page, text="Username : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").grid(row=2, column=0, pady=5)
    #Entry(reg_page, textvariable=username).grid(row=2, column=1, pady=5)
    #Label(reg_page, bg="#f0fff0").grid(row=3, column=0, pady=5)
    #Label(reg_page, text="Password : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").grid(row=4, column=0, pady=5)
    #Entry(reg_page, textvariable=password, show="*").grid(row=4, column=1, pady=5)
    #Button(reg_page, text="Register", font=("Helvetica", 12), bg="light green", fg="dark green", command=register_user).grid(row=5, column=0, columnspan=2, pady=10)
    Label(reg_page, text="Register Your Account", font=("Helvetica", 12), bg="#f0fff0", fg="dark green", width=300).pack()

    Label(reg_page,bg="#f0fff0").pack()
    Label(reg_page, text="Username : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Entry(reg_page, textvariable=username).pack()
    Label(reg_page,bg="#f0fff0").pack()
    Label(reg_page, text="Password : ", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Entry(reg_page, textvariable=password, show="*").pack()
    Button(reg_page, text="Register", font=("Helvetica", 12), bg="light green", fg="dark green", command=register_user).pack()

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

        Label(root, bg="#f0fff0").grid(row=0, column=0)  # Adjust the row and column as needed
        root.update_idletasks()  # Ensure GUI updates before sleeping
        root.after(1000, success)  # Use root.after() to delay the success function instead of time.sleep()

def error():
    global err
    err = tk.Frame(root)
    err.grid()
    err.configure(bg="#f0fff0")
 #   Label(err, text="All fields are required...", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").grid(row=0, column=0, columnspan=2)
#    Label(err, bg="#f0fff0").grid(row=1, column=0)
#    Button(err, text="OK", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=error_destroy).grid(row=2, column=0, columnspan=2, pady=5)
    Label(err, text="All fields are required...", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Label(err,bg="#f0fff0").pack()
    Button(err, text="OK", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=error_destroy).pack()

def success():
    global succ
    succ =tk.Frame(root)
    succ.grid()
    succ.configure(bg="#f0fff0")
    Label(succ, text="Registration successful...", font=("Helvetica", 12), bg="#f0fff0", fg="dark green").pack()
    Label(succ,bg="#f0fff0").pack()
    Button(succ, text="OK", font=("Helvetica", 12), bg="light green", fg="dark green", width=8, height=1, command=succ_destroy).pack()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    reg_page.destroy()