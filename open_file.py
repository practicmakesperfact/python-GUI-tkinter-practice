from tkinter import *
from tkinter import filedialog

def openFile():
    filepath=filedialog.askopenfilename()
    file=open(filepath,'r')
    print(file.read())
    file.close()
    
    
window = Tk()

Button = Button(text="open", command=openFile)
Button.pack()

window.mainloop()


