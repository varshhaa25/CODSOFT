import tkinter as tk
from tkinter import *

#tkinter window
win=Tk()
win.title("Calculator")
win.geometry("450x450")
win.configure(bg="black")

exp=""
input1=tk.StringVar()

entry1= tk.Entry(win,font=('cambria',18,),textvariable=input1,width=50,bg='black',fg='white',highlightthickness=2,highlightcolor='grey',bd=2,justify=tk.RIGHT)
entry1.pack(ipady=10)

#calculator window
calc1=tk.Frame(win,width=400,height=400,bg="grey")
calc1.pack()

def btn_click(item):
    global exp
    exp+=str(item)
    input1.set(exp)

def btn_delete():
    global exp
    exp=exp[:-1]  
    input1.set(exp)

def btn_clear():
    global exp
    exp=""
    input1.set("")

def btn_equal():
    global exp
    try:
        res=str(eval(exp))
        input1.set(res)
        exp=res
    except:
        input1.set("Error")
        exp=""

#common for buttons
num_btn={'fg':'white','height':3,'bd':0,'bg':'black','cursor':'arrow'}
opr_btn=num_btn.copy()
opr_btn.update({'bg':'orange','fg':'black'})

#first row
clear=tk.Button(calc1,text="C",width=20,command=btn_clear,**num_btn)
clear.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="nsew")

delete=tk.Button(calc1,text="DEL",width=10,command=btn_delete,**num_btn)
delete.grid(row=0,column=2,padx=5,pady=5,sticky="nsew")

divide=tk.Button(calc1,text="/",width=10,command=lambda:btn_click("/"),**opr_btn)
divide.grid(row=0,column=3,padx=5,pady=5,sticky="nsew")

#second row
seven=tk.Button(calc1,text="7",command=lambda:btn_click(7),**num_btn)
seven.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")

eight=tk.Button(calc1,text="8",command=lambda:btn_click(8),**num_btn)
eight.grid(row=1,column=1,padx=5,pady=5,sticky="nsew")

nine=tk.Button(calc1,text="9",command=lambda:btn_click(9),**num_btn)
nine.grid(row=1,column=2,padx=5,pady=5,sticky="nsew")

multiply=tk.Button(calc1,text="*",command=lambda:btn_click("*"),**opr_btn)
multiply.grid(row=1,column=3,padx=5,pady=5,sticky="nsew")

#third row
four=tk.Button(calc1,text="4",command=lambda:btn_click(4),**num_btn)
four.grid(row=2,column=0,padx=5,pady=5,sticky="nsew")

five=tk.Button(calc1,text="5",command=lambda:btn_click(5),**num_btn)
five.grid(row=2,column=1,padx=5,pady=5,sticky="nsew")

six=tk.Button(calc1,text="6",command=lambda:btn_click(6),**num_btn)
six.grid(row=2,column=2,padx=5,pady=5,sticky="nsew")

minus=tk.Button(calc1,text="-",command=lambda:btn_click("-"),**opr_btn)
minus.grid(row=2,column=3,padx=5,pady=5,sticky="nsew")

#fourth row
one=tk.Button(calc1,text="1",command=lambda:btn_click(1),**num_btn)
one.grid(row=3,column=0,padx=5,pady=5,sticky="nsew")

two=tk.Button(calc1,text="2",command=lambda:btn_click(2),**num_btn)
two.grid(row=3,column=1,padx=5,pady=5,sticky="nsew")

three=tk.Button(calc1,text="3",command=lambda:btn_click(3),**num_btn)
three.grid(row=3,column=2,padx=5,pady=5,sticky="nsew")

plus=tk.Button(calc1,text="+",command=lambda:btn_click("+"),**opr_btn)
plus.grid(row=3,column=3,padx=5,pady=5,sticky="nsew")

#fifth row
zero=tk.Button(calc1,text="0",width=21,command=lambda:btn_click(0),**num_btn)
zero.grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky="nsew")

point=tk.Button(calc1, text=".",command=lambda:btn_click("."),**num_btn)
point.grid(row=4,column=2,padx=5,pady=5,sticky="nsew")

equal=tk.Button(calc1, text="=",command=btn_equal,**opr_btn)
equal.grid(row=4,column=3,padx=5,pady=5,sticky="nsew")

win.mainloop()
