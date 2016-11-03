import math
def metodo():
  valor=int(input("Elija la función que desea utilizar:\n 1.Suma \n 2. Resta \n 3. Multiplicacion\n 4. Division\n 5. Sen(x) \n 6. Cos(x)\n 7. Tan(x)\n 8. ln \n 9. potencia \n 10.  Salir "))
  if(valor==1):
    valor1=float(input("Primer numero: "))
    valor2=float(input("Segundo numero: "))
    valortotal=valor1+valor2
    print("El resultado es: "+str(valortotal))
  elif(valor==2):
    valor1=float(input("Primer numero: "))
    valor2=float(input("Segundo numero: "))
    valortotal=valor1-valor2
    print("El resultado es: "+str(valortotal))
  elif(valor==3):
    valor1=float(input("Primer numero: "))
    valor2=float(input("SEgundo numero: "))
    valortotal=valor1*valor2
    print("El resultado es: "+str(valortotal))
  elif(valor==4):
    valor1=float(input("Primer numero: "))
    valor2=float(input("Segundo numero: "))
    valortotal=valor1/valor2
    print("EL resultado es: "+str(valortotal))
  elif(valor==5):
    valor1=float(input("El numero en radianes es: "))
    valortotal=math.sin(valor1)
    print("El resultado es: "+str(valortotal))
  elif(valor==6):
    valor1=float(input("El numero en radianes es: "))
    valortotal=math.cos(valor1)
    print("EL resultado es: "+str(valortotal))
  elif(valor==7):
    valor1=float(input("El numero en radianes es: "))
    valortotal=math.tan(valor1)
    print("El resultado es: "+str(valortotal))
  elif(valor==8):
    valor1=float(input("El numero al que le desea sacar el ln es: "))
    valortotal=math.log1p(valor1)
    print("EL resultado es: "+str(valortotal))
  elif(valor==9):
    valor1=float(input("Ingrese el primer numero: "))
    valor2=float(input("Ingrese el segundo numero: "))
    valortotal=math.pow(valor1,valor2)
    print("EL resultado es: "+str(valortotal))
  return valor
while(metodo()!=10):
 pass

