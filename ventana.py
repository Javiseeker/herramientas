import tkinter as tk
from tkinter import ttk
def on_click():
	label1.configure(text="Te dije que no   "+name.get())
	label1.configure(foreground='red')
	label1.configure(background='gold')
	boton.configure(state='disable')
pass
win = tk.Tk()
win.title("Hola GUI")
win.resizable(0,0)
#ttk.Label(win,text="Hola etiqueta").grid(row=0,column=0)
#ttk.Label(win,text="Diego F. Chavarro Sanchez").grid(row=0,column=1)
#ttk.Button(win,text="Click me",comman=on_click).grid(row=1,column=1)
label1=ttk.Label(win,text="Hola Label")
label1.grid(row=0,column=0)
boton=ttk.Button(win,text="Don't click me",comman=on_click)
boton.grid(row=1,column=1)
name=tk.StringVar()
txtentry=ttk.Entry(win,textvariable=name)
txtentry.grid(row=1,column=0)

win.mainloop()
