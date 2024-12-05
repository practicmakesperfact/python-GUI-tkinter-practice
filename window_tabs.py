from tkinter import *
from tkinter import ttk


window= Tk()

notebook = ttk.Notebook(window)   # MANAGE ALL WEDGIT  COLLECTION'S
tab1 = Frame(notebook)    
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab1")   # new frame for tab 1
notebook.add(tab2, text="Tab2")    # new frame for tab 2

notebook.pack(expand=True, fill=BOTH) # both fill both x and y axise and stick in top left corner 
                                       # expand gives expansion 
Label(tab1, text="Hello, this is tab #1", width=50, height=25).pack()  #add text for tabe 1
Label(tab2, text="Goodbye, this is tab #2", width=50,height=25).pack()     #add text for tabe 2

window.mainloop()