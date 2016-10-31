import tkinter as tk
from tkinter import ttk
def boton0on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"0")
pass
def botonpuntoon_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+".")
pass
def boton1on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"1")
pass
def boton2on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"2")
pass
def boton3on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"3")
pass
def boton4on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"4")
pass
def boton5on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"5")
pass
def boton6on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"6")
pass
def boton7on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"7")
pass
def boton8on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"8")
pass
def boton9on_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set(textoActual+"9")
pass

def botondivisionon_click():
	global numero
	global opc
	numero=float(label0Text.get())
	opc='4'
	label0Text.set("")
pass
def botonmultiplicacionon_click():
	global numero
	global opc
	numero=float(label0Text.get())
	opc='3'
	label0Text.set("")
pass
def botonrestaon_click():
	global numero
	global opc
	numero=float(label0Text.get())
	opc='2'
	label0Text.set("")
pass
def botonsumaon_click():
	 global numero
	 numero=float(label0Text.get())
	 global opc
	 opc='1'
	 label0Text.set("")
pass
def botonreseton_click():
	global textoActual
	textoActual=label0Text.get()
	label0Text.set("")
pass
def to_num(string):
	print(string)
	try:
		return float(string)
	except ValueError:
		return int(string)

def botonigualon_click():
 global numero
 global textoActual
 global opc
 textoActual=label0Text.get()
 if opc=='1':
   ope=	to_num(str(numero))+to_num(str(textoActual))
   label0Text.set(str(ope))
 if opc=='2':
   ope=to_num(str(numero))-to_num(str(textoActual))
   label0Text.set(str(ope))
 if opc=='3':
   ope=to_num(str(numero))*to_num(str(textoActual))
   label0Text.set(str(ope))
 if opc=='4':
   ope=to_num(str(numero))/to_num(str(textoActual))
   label0Text.set(str(ope))
pass
win = tk.Tk()
win.title("Calculadora OP")
win.resizable(0,0)
#ttk.Label(win,text="Hola etiqueta").grid(row=0,column=0)
#ttk.Label(win,text="Diego F. Chavarro Sanchez").grid(row=0,column=1)
#ttk.Button(win,text="Click me",comman=on_click).grid(row=1,column=1)
#label1=ttk.Label(win,text="Hola Label")
#label1.grid(row=4,column=2)
opc='0'
numero=0.0
textoActual=0.0
boton0=ttk.Button(win,text="0",comman=boton0on_click)
boton0.grid(row=5,column=2)
botonpunto=ttk.Button(win,text=".",comman=botonpuntoon_click)
botonpunto.grid(row=5,column=3)
boton1=ttk.Button(win,text="1",comman=boton1on_click)
boton1.grid(row=4,column=1)
boton2=ttk.Button(win,text="2",comman=boton2on_click)
boton2.grid(row=4,column=2)
boton3=ttk.Button(win,text="3",comman=boton3on_click)
boton3.grid(row=4,column=3)
boton4=ttk.Button(win,text="4",comman=boton4on_click)
boton4.grid(row=3,column=1)
boton5=ttk.Button(win,text="5",comman=boton5on_click)
boton5.grid(row=3,column=2)
boton6=ttk.Button(win,text="6",comman=boton6on_click)
boton6.grid(row=3,column=3)
boton7=ttk.Button(win,text="7",comman=boton7on_click)
boton7.grid(row=2,column=1)
boton8=ttk.Button(win,text="8",comman=boton8on_click)
boton8.grid(row=2,column=2)
boton9=ttk.Button(win,text="9",comman=boton9on_click)
boton9.grid(row=2,column=3)
botondivision=ttk.Button(win,text="÷",comman=botondivisionon_click)
botondivision.grid(row=2,column=4)
botonmultiplicacion=ttk.Button(win,text="x",comman=botonmultiplicacionon_click)
botonmultiplicacion.grid(row=3,column=4)
botonresta=ttk.Button(win,text="-",comman=botonrestaon_click)
botonresta.grid(row=4,column=4)
botonsuma=ttk.Button(win,text="+",comman=botonsumaon_click)
botonsuma.grid(row=5,column=4)
botonreset=ttk.Button(win,text="CE",comman=botonreseton_click)
botonreset.grid(row=2,column=5)
botonigual=ttk.Button(win,text="=",comman=botonigualon_click)
botonigual.grid(row=3,column=5)
label0Text=tk.StringVar()
txtentry=ttk.Entry(win,textvariable=label0Text)
txtentry.grid(row=1)
win.mainloop()
