from tkinter import *
import tkinter as tk
from login.login_gui import *

def show_frame(frame):
    frame.tkraise()

def main_screen():
    global root,main_page,login_page,reg_page
    root = tk.Tk()
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    root.title("Login Portal")
    root.geometry("300x300")

    main_page = tk.Frame(root,bg="#f0fff0")
    reg_page = tk.Frame(root,bg="#f0fff0")
    login_page = login_frame(root, show_frame)

    for page in (main_page, reg_page, login_page):
        page.grid(row=0,column=0,sticky='nsew')

    Label(main_page, text="Welcome to the login portal", font=("Helvetica", 12), bg="#f0fff0", fg="dark green", width=30).pack()
    Label(main_page,bg="#f0fff0").pack()
    Button(main_page, text="Log-In", height=1, font=("Helvetica", 12), bg="light green", fg="dark green", width=8,command=lambda:show_frame(login_page)).pack()
    Label(main_page,bg="#f0fff0").pack()
    Button(main_page, text="Registration", height=1, font=("Helvetica", 12), bg="light green", fg="dark green", width=15, command=lambda:show_frame(reg_page)).pack()
    Label(main_page,bg="#f0fff0").pack()
    show_frame(main_page)
    root.mainloop()
    return root, main_page, login_page, reg_page

if __name__ == "__main__":
    main_screen()