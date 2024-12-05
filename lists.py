#  listbox

def submit():
    food= []
    for index in Listbox.curselection():
        food.insert(index, Listbox.get(index))
    print("you have ordered: ")
    for index in food:
        print(index)


def add():
    Listbox.insert(Listbox.size(),entrybox.get())
def Delete():
   for index in reversed(Listbox.curselection()):
       Listbox.delete(index)
       
       Listbox.config(height=Listbox.size())
    
from tkinter import *


window = Tk()
Listbox = Listbox(window,
                    bg="#ffed44",
                    font=("arial", 30),
                    width=12,
                    selectmode=MULTIPLE
                    )
Listbox.config(height=Listbox.size())

entrybox=Entry(window)

submitButton = Button(window, text="submit" , command=submit)
AddButton = Button(window, text="Add" , command=add)
deleteButton = Button(window, text="delete" , command=Delete)

Listbox.insert(1, "piza")
Listbox.insert(2, "burger")
Listbox.insert(3, "tibs")
Listbox.insert(4, "dulet")
Listbox.insert(5, "chakolat")
Listbox.insert(6, "kitfo")
Listbox.pack()
entrybox.pack()
submitButton.pack()
AddButton.pack()
deleteButton.pack()
window.mainloop()