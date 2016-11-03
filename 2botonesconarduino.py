import tkinter as tk
from tkinter import ttk
import serial
puerto=serial.Serial('/dev/ttyACM0',9600,timeout=1)
def boton1on_click():
	global puerto
	puerto.write("a".encode())
pass
def boton2on_click():
	global puerto
	puerto.write("z".encode())
pass
win=tk.Tk()
win.title("Prueba X Arduino")
win.resizable(0,0)
label=ttk.Label(win,text="Quiubo")
boton1=ttk.Button(win,text="Prender",command=boton1on_click)
boton1.grid(row=0,column=0)
boton2=ttk.Button(win,text="Apagar",command=boton2on_click)
boton2.grid(row=1,column=0)
win.mainloop()
