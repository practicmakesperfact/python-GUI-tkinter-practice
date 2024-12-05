from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB =100
    download = 0
    speed = 1
    while (download < GB):
        
        time.sleep(0.05)
        
        bar['value']+=(speed/GB)*100
        download+=speed 
        percent.set(str(int((download/GB)*100 ))+ "%")
        Text.set(str(download)+"/"+str(GB)+ " GB Completed")
        window.update_idletasks()
        
        
window=Tk()
percent=StringVar()
Text=StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=20)

Label(window,textvariable=percent ,font="arial").pack()
Label(window,textvariable=Text , font=("arial")).pack()
Button(window, text="Download",command=start).pack()
window.mainloop()
 
 
