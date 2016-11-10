import tkinter as tk
from tkinter import ttk
import serial
puerto=serial.Serial('\dev\ttyACM0',9600,time=1)
def on_click():
	global puerto
	puerto.open()
	val=puerto.read()
	if(int(val)>300):
		label1.configure(Background='White')
		if(int(val)>600):
			label2.configure(Background='Black')
		else: 
			label2<='Black'
	else:
		label2<='Black'
	puerto.close
pass
win=tk.Tk()
win.title("Muestra")
win.resizable(0,0)
label1=ttk.Label(win)
label1.grid(row=0,column=0)
label2=ttk.Label(win)
label2.grid(row=1,column=0)
label3=ttk.Label(win)
label3.grid(row=2,column=0)
label4=ttk.Label(win)
label4.grid(row=3,column=0)
boton1=ttk.Button(win,text="1",command=on_click)
boton1.grid(row=4,column=4)
win.mainloop()
