from tkinter import *

def resize(ev=None):
    label.config(font="Helvetica -%d bold"%scale.get())

top=Tk()
top.geometry('250x100')
label=Label(top,text="Hello World!",font="Helvetica 10 bold")
label.pack()
scale=Scale(top,from_=40,to=100,orient=HORIZONTAL,command=resize)
scale.pack()
top.mainloop
