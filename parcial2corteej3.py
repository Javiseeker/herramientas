x=int(input("Primera base: "))
y=int(input("Segunda base: "))
z=int(input("Tercera base: "))
mod=int(input("Escoja el modulo de la bases que ingresó: "))
f=int(x%mod)
g=int(y%mod)
h=int(z%mod)
print("1. Suma de Residuos\n 2. Resta de Residuos\n 3. Multiplicación de Residuos\n")
seleccion=int(input("Ingrese el numero deseado del menu: "))
if(seleccion==1):
 resultado=int(f+g+h)
 print("La suma de residuos es: "+str(resultado))
elif(seleccion==2):
 resultado=int(f-g-h)
 print("La resta de residuos es: "+str(resultado))
elif(seleccion==3):
 resultado=int(f*g*h)
 print("La multiplicacion de residuos es: "+str(resultado))
