from tkinter import *

window= Tk()

Frame = Frame(window, bg="pink",relief=SUNKEN)
Frame.pack()

Button(Frame,text="W",font=("san-serif",25),width=3).pack(side=TOP)
Button(Frame,text="A",font=("san-serif",25),width=3).pack(side=LEFT)
Button(Frame,text="S",font=("san-serif",25),width=3).pack(side=LEFT)
Button(Frame,text="D",font=("san-serif",25),width=3).pack(side=LEFT)

mainloop()