from tkinter import Label, Button
import tkinter as tk
import registration
import login
def main_screen():
    global root
    root = tk.Tk()
    root.title("Login Portal")
    root.configure(bg="#f0fff0")
    root.geometry("300x300")
    Label(root, text="Welcome to the login portal", font=("Helvetica", 12), bg="#f0fff0", fg="dark green", width=30).pack()
    Label(root,bg="#f0fff0").pack()
    Button(root, text="Log-In", height=1, font=("Helvetica", 12), bg="light green", fg="dark green", width=8, command=login).pack()
    Label(root,bg="#f0fff0").pack()
    Button(root, text="Registration", height=1, font=("Helvetica", 12), bg="light green", fg="dark green", width=15, command=registration).pack()
    Label(root,bg="#f0fff0").pack()
    root.mainloop()

if __name__ == "__main__":
    main_screen()