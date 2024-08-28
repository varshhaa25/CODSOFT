import tkinter as tk
from tkinter import messagebox
import random
import string

win=tk.Tk()
win.geometry("400x400")
win.configure(bg="thistle")
win.title("Password Generator")

hlabel=label1=tk.Label(win,text="PASSWORD GENERATOR",bg="plum3",font=("Times New Roman",15))
hlabel.pack()

label1=tk.Label(win,text="Password length",bg="plum3",font=("Times New Roman",15))
label1.pack(pady=20)

entry1=tk.Entry(win,width=10,bg="thistle1")
entry1.pack(pady=1)

def password():
    try:
        length=int(entry1.get())
        if length<1:
            messagebox.showwarning("Invalid Input","Please enter a positive integer")
    except ValueError:
        messagebox.showwarning("Invalid Input","Please enter a valid integer")
        return
    
    chars=string.ascii_letters+string.digits+string.punctuation
    pwd=''.join(random.choice(chars) for i in range(length))

    label3.config(text=pwd)

def pwd_copy():
    pwd=label3.cget("text")
    if pwd:
        win.clipboard_clear()
        win.clipboard_append(pwd)
        messagebox.showinfo("Copied","Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password","Please generate a password first")
    

button1=tk.Button(win,text="Generate Password",bg="thistle1",font=('Times New Roman',13),command=password)
button1.pack(pady=10,ipady=1)

label2= tk.Label(win,text="Generated Password",bg="plum3",font=("Times New Roman",15))
label2.pack(pady=20)

label3=tk.Label(win,text="",bg="thistle1",width=30,font=("Times New Roman",15))
label3.pack(pady=1)

button_copy=tk.Button(win,text="Copy",bg="thistle1",font=("Times New Roman",13),command=pwd_copy)
button_copy.pack(pady=10)

win.mainloop()
