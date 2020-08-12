import tkinter
from tkinter import *
import random
from tkinter import messagebox


answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "mexico",
    "legend",
    "dragon",
    "well",
    "king"
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "ixocem",
    "delegn",
    "nodgra",
    "lewe",
    "inkg",
]

num = random.randrange(0,10,1)

def res():
    global words,answers,num
    num = random.randrange(0,10,1)
    lb1.config(text=words[num])
    e1.delete(0,END)

def default():
    global words,answers,num
    lb1.config(text=words[num])

def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success","this is a correct answer")
        res()
    else:
        messagebox.showerror("ERROR","this is not correct ")   
        e1.delete(0, END)






root=tkinter.Tk()
root.geometry("330x400")
root.title("Jumbled")
root.configure(background="black")



lb1= Label(
    root,
    text="Your here",
    font=("Verdana",18),
    bg="#000000",
    fg="#ffffff",
)

lb1.pack(pady=30,ipady=10,ipadx=10)

ans1 = StringVar()
e1=Entry(
    root,
    font=("Verdana",16),
    textvariable = ans1,
)

e1.pack(ipady=5,ipadx=5)

btncheck = Button(
    root,
    text="check",
    font=("Comic sans ms", 16),
    width=16,
    bg="grey",
    fg="dark green",
    command=checkans,
    
)

btncheck.pack(pady=40)


btnreset=Button(
    root,
    text="Reset",
    font=("Comic sans ms", 16),
    width=16,
    bg="grey",
    fg="red",
    command=res,

)

btnreset.pack()

default()

root.mainloop()