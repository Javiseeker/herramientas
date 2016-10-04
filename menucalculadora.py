valor=int(input("Elija la función que desea utilizar:\n 1.Suma \n 2. Resta \n 3. Multiplicacion "))
if(valor==1):
  valor1=int(input("Primer numero: "))
  valor2=int(input("Segundo numero: "))
  valortotal=valor1+valor2
  print("El resultado es: "+str(valortotal))
elif(valor==2):
  valor1=int(input("Primer numero: "))
  valor2=int(input("Segundo numero: "))
  valortotal=valor1-valor2
  print("El resultado es: "+str(valortotal))
elif(valor==3):
  valor1=int(input("Primer numero: "))
  valor2=int(input("SEgundo numero: "))
  valortotal=valor1*valor2
  print("El resultado es: "+str(valortotal))
elif(valor<0 and valor>3):
  print("NO existe esa opcion")

