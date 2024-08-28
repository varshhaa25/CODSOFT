import tkinter as tk
from tkinter import *
from datetime import datetime
from tkinter import messagebox
import os

win=tk.Tk()
win.geometry("500x500")
win.configure(bg="skyblue4")
win.title("To-Do List")

label1=tk.Label(win,text="TO-DO LIST",bg="skyblue4",fg="white",font=("Times New Roman",15,"bold"))
label1.pack(pady=5,anchor="center")

date_frame=tk.Frame(win,bg="skyblue4")
date_frame.pack(side=tk.TOP,anchor="ne")

label2=tk.Label(date_frame,text="Date",bg="skyblue4",fg="white",font=("Times New Roman",15,"bold"))
label2.pack(side=tk.TOP,anchor="ne")

curr_date=datetime.now().strftime("%Y-%m-%d")
label3=tk.Label(date_frame,text=curr_date,bg="skyblue4",fg="white",font=("Times New Roman",15,"bold"))
label3.pack(side=tk.TOP,anchor="ne")

#task entry box
label4=tk.Label(text="Enter your tasks here",bg="skyblue4",fg="white",font=("Times New Roman",15))
label4.pack(pady=10)

entry=tk.Entry(win,width=50,bg="alice blue")
entry.pack(pady=2,ipady=5)

#date entry
label5=tk.Label(text="Due date",bg="skyblue4",fg="white",font=("Times New Roman",15))
label5.pack(pady=10)

date_entry=tk.Entry(win,width=20,bg="alice blue")
date_entry.pack(pady=0.5,ipady=5)
date_entry.insert(0,"YYYY-MM-DD")

def on_click(event):
    if date_entry.get()=="YYYY-MM-DD":
        date_entry.delete(0,tk.END)
        date_entry.config(fg='black')

def on_focusout(event):
    if date_entry.get()=="":
        date_entry.insert(0,"YYYY-MM-DD")
        date_entry.config(fg='grey')

date_entry.bind("<FocusIn>",on_click)
date_entry.bind("<FocusOut>",on_focusout)

def save_tasks():
    with open('tasks.txt','w') as file:
        for item in todo_list.get(0,tk.END):
            file.write(item+'\n')

def load_tasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt','r') as file:
            for line in file:
                todo_list.insert(tk.END,line.strip())

#functions to manipulate tasks
def sort_task(task,due_date):
    new_task=f"{task} (Due: {due_date})"
    insrtd=False
    for i in range(todo_list.size()):
        task1=todo_list.get(i)
        due_date1=task1.split("Due: ")[1].strip().replace(")","")
        if datetime.strptime(due_date,"%Y-%m-%d")< datetime.strptime(due_date1,"%Y-%m-%d"):
            todo_list.insert(i,new_task)
            insrtd=True
            break
    if not insrtd:
        todo_list.insert(tk.END,new_task)

def add_task():
    task=entry.get()
    due_date=date_entry.get()
    if task!="" and due_date!="":
        try:
            datetime.strptime(due_date,"%Y-%m-%d")
            sort_task(task,due_date)
            entry.delete(0,tk.END)
            date_entry.delete(0,tk.END)
        except ValueError:
            messagebox.showwarning("Warning","Please enter a valid date in YYYY-MM-DD format")
    else:
        messagebox.showwarning("Warning","Please enter a task and a due date")

def edit_task():
    try:
        selected=todo_list.curselection()[0]
        new_task=entry.get()
        new_due_date=date_entry.get()
        if new_task!="" and new_due_date!="":
            try:
                datetime.strptime(new_due_date,"%Y-%m-%d")
                todo_list.delete(selected)
                sort_task(new_task,new_due_date)
                entry.delete(0,tk.END)
                date_entry.delete(0,tk.END)
            except ValueError:
                messagebox.showwarning("Warning","Please enter a valid date in YYYY-MM-DD format")
        else:
            messagebox.showwarning("Warning","Please enter a new task and due date")
    except:
        messagebox.showwarning("Warning","Please select a task to edit")

        
'''def add_task():
    task=entry.get()
    due_date=date_entry.get()
    if task!="" and due_date!="":
        try:
            datetime.strptime(due_date,"%Y-%m-%d")
            todo_list.insert(tk.END,f"{task} (Due: {due_date})")
            entry.delete(0,tk.END)
            date_entry.delete(0,tk.END)
        except ValueError:
            messagebox.showwarning("Warning","Please enter a valid date in YYYY-MM-DD format")
    else:
        messagebox.showwarning("Warning","Please enter a task and a due date")

def edit_task():
    try:
        selected=todo_list.curselection()[0]
        new_task=entry.get()
        new_due_date=date_entry.get()
        if new_task!="" and new_due_date!="":
            try:
                datetime.strptime(new_due_date,"%Y-%m-%d")
                todo_list.delete(selected)
                todo_list.insert(selected,f"{new_task} (Due: {new_due_date})")
                entry.delete(0,tk.END)
                date_entry.delete(0,tk.END)
            except ValueError:
                messagebox.showwarning("Warning","Please enter a valid date in YYYY-MM-DD format")
        else:
            messagebox.showwarning("Warning","Please enter a new task and due date")
    except:
        messagebox.showwarning("Warning","Please select a task to edit")'''

def delete_task():
    try:
        selected=todo_list.curselection()[0]
        todo_list.delete(selected)
    except:
        messagebox.showwarning("Warning","Please select a task")

def complete_task():
    try:
        selected=todo_list.curselection()[0]
        task=todo_list.get(selected)
        todo_list.delete(selected)
        todo_list.insert(tk.END,task+" - done")
    except:
        messagebox.showwarning("Warning","Please select a task")

#todo list
frame1=Frame(win,width=50,height=5)
frame1.pack(pady=10)

todo_list=tk.Listbox(frame1,width=50,height=5,bg="alice blue",font=("Times New Roman",12))
todo_list.pack(side=LEFT,fill=BOTH)

#scrollbar
scrollbar1= Scrollbar(frame1)
scrollbar1.pack(side=RIGHT, fill=BOTH)
todo_list.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=todo_list.yview)

#buttons
button_frame1=tk.Frame(win,bg="skyblue4")
button_frame1.pack(pady=10)

add_btn=tk.Button(button_frame1,text="Add Task",width=20,bg="alice blue",command=add_task)
add_btn.grid(row=0,column=0,padx=5,pady=5)

edit_btn=tk.Button(button_frame1,text="Edit Task",width=20,bg="alice blue",command=edit_task)
edit_btn.grid(row=0,column=1,padx=5,pady=5)

complete_btn=tk.Button(button_frame1,text="Complete Task",width=20,bg="alice blue",command=complete_task)
complete_btn.grid(row=1,column=0,padx=5,pady=5)

delete_btn=tk.Button(button_frame1, text="Delete Task", width=20,bg="alice blue",command=delete_task)
delete_btn.grid(row=1,column=1,padx=5,pady=5)

#loading tasks when application starts
load_tasks()

#saving tasks when application exits
win.protocol("WM_DELETE_WINDOW",lambda:[save_tasks(),win.destroy()])

win.mainloop()
