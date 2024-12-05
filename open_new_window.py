from tkinter import *

def createNewWindow():   # to methods to create new window the first one using new_window = toplevel() at this time create new window at the top but when you close the bottom or firts window it also close
                          # the second method is tk()  method this is not close while the first close 
    new_window= Tk()
    window.destroy()  # is is used to close the first window after creating the second

window = Tk()

Button(window,text="open new window", command=createNewWindow).pack()

window.mainloop()