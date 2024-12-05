from tkinter import *
from tkinter import colorchooser

def click():
    # color = colorchooser.askcolor()
    # print(color)
    #colorHex =color[1]    #[1] used to retrive hexaDecimal color value
    # print(colorHex)
    # window.config(bg=colorHex)
    # window.config(bg=color[1])
    window.config(bg=colorchooser.askcolor()[1])

window= Tk()
window.geometry("420x420")
Button = Button(window, text="click me",command=click)

Button.pack()

window.mainloop()