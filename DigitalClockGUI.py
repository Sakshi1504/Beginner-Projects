import tkinter
import time
from tkinter import Label, Tk

app_window=Tk()
app_window.title("Digital Clock")
app_window.geometry("250x250")
app_window.resizable(1,1)


textfont=("Boulder", 68, 'bold')
fc="#000000"
bc="#FFC0CB"
bdw=25

label=Label(app_window, font=textfont, foreground=fc, background=bc, borderwidth=bdw)
label.grid(row=0, column=1)

def digitalclock():
    currenttime=time.strftime("%H:%M:%S")
    label.config(text=currenttime)
    label.after(200, digitalclock)


digitalclock()
app_window.mainloop()