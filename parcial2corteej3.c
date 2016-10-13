#include <stdio.h> 
int main(){
int mod, x, y, z, f, g, h, seleccion, resultado;
printf("Ingrese base 1: ");
scanf("%d",&x);
printf("Ingrese base 2: ");
scanf("%d",&y);
printf("Ingrese base 3: ");
scanf("%d",&z);
printf("Escoja el modulo de las bases ingresadas: ");
scanf("%d",&mod);
f=x%mod;
g=y%mod;
h=z%mod;
printf("1. Suma de los residuos\n 2. Resta de los residuos\n 3. Multiplicacion de los residuos\n");
scanf("%d",&seleccion);
if(seleccion==1){
resultado= f+g+h;
printf("La suma del residuo es: %d",resultado);
}
else if(seleccion==2){
resultado=f-g-h;
printf("La resta del residuo es: %d",resultado);
}
else if(seleccion==3){
resultado=f*g*h;
printf("La multiplicacion del residuo es: &d",resultado);
}
}
