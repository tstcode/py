from tkinter import *

top=Tk()

def go(ev=None):
 label.config(text="Go...",font="Helvetica 20 bold",fg="green")

def wait(ev=None):
 label.config(text="Wait...",font="Helvetica 20 bold",bg="pink",fg="yellow")

def stop(ev=None):
 label.config(text="STOP!!",font="Helvetica 20 bold",bg="red")

label=Label(top,text='')
label.pack()
b1=Button(top,text="Go..",font="Helvetica 10 bold",fg="green",command=go)
b1.pack()
b2=Button(top,text="Wait..",font="Helvetica 10 bold",bg="pink",fg="yellow",command=wait)
b2.pack()
b3=Button(top,text="STOP!!",font="Helvetica 10 bold",fg="red",command=stop)
b3.pack()
top.mainloop()
