from tkinter import *
import tkinter as tk
import registration
import login
def main_screen():
    global root,main_page
    root = tk.Tk()
    root.title("Login Portal")
    root.geometry("300x300")
    root.configure(bg="#f0fff0")
    main_page=Frame(root)
    main_page.pack()
    main_page.configure(bg="#f0fff0")
    Label(main_page, text="Welcome to the login portal", font=("Helvetica", 12), bg="#f0fff0", fg="dark green", width=30).pack()
    Label(main_page,bg="#f0fff0").pack()
    Button(main_page, text="Log-In", height=1, font=("Helvetica", 12), bg="light green", fg="dark green", width=8, command=login).pack()
    Label(main_page,bg="#f0fff0").pack()
    Button(main_page, text="Registration", height=1, font=("Helvetica", 12), bg="light green", fg="dark green", width=15, command=lambda:registration.tkraise()).pack()
    Label(main_page,bg="#f0fff0").pack()
    root.mainloop()

if __name__ == "__main__":
    main_screen()