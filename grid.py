from tkinter import *
 
 
 
window= Tk()
window.title("User Info")
# titleLabel = Label(window, text="Enter Your Information") 
 # titleLabel.grid(row=0,column=0,columnspan=2)  or in short 
Label(window, text="Enter Your Information").grid(row=0,column=0,columnspan=2)
 
Label(window, text="First Name" ,fg="red").grid(row=1,column=0) 
Entry().grid(row=1,column=1)

Label(window, text="Last Name",fg="orange").grid(row=2,column=0) 
Entry().grid(row=2,column=1)

Label(window, text="Email ",fg="aqua").grid(row=3,column=0) 
Entry().grid(row=3,column=1)

Label(window, text="phone ",fg="green").grid(row=4,column=0) 
Entry().grid(row=4,column=1)
 
Button(window,text="Submit",bg="black", fg="white", font=("arial,25")).grid(row=5,column=0,columnspan=2)
window.mainloop()
 
 