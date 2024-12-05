from tkinter import *
from tkinter import messagebox
def click():
    # messagebox.showinfo(title='this is an info message',message='you are a person')
    # messagebox.showwarning(title='this is a warning',message='you are virus!!!')
    # messagebox.showerror(title='ERROR',message='semthing wents wrong')
    # if messagebox.askokcancel(title='ask ok cancel',message='you do it?'):
    #     print('Great!, you did it.')
    # else:
    #     print("Oh, you didn't do it.")
    
    # if messagebox.askretrycancel(title='ask retry cancel',message='you retry the thing ?'):
    #     print('Great!, you retry it.')
    # else:
    #     print("Oh, you canceled retry ")
    
    # if messagebox.askyesno(title='ask yes or no',message='do you like pizza ?'):
    #     print('i like pizza!')
    # else:
    #     print("why you don't like pizza ")
    
    # print(messagebox.askquestion(title='ask question ', message='do you like cake ?'))
    print(messagebox.askyesnocancel(title='ask question ', message='do you like code ?'))
    

window = Tk()

Button = Button(window, command=click , text='click me')
Button.pack()

window.mainloop()