#include <stdio.h>
int main(){
int a,b,c,r,d,g,e;

do{
printf("Escoja la opción que necesite:\n 1. Suma\n 2. Resta\n 3. Multiplicación\n 4. División\n 5. Potencia\n 6. Salir\n");
scanf("%d",&a);
if(a<=0 || a>6){
printf("Valor incorrecto; se apaga el programa!");
}
else{
switch(a){
case 1:
printf("Ingrese el primer numero: ");
scanf("%d",&b);
printf("Ingrese el segundo numero: ");
scanf("%d",&c);
r=b+c;
printf("El resultado es %d",r);
break;
case 2:
printf("Ingrese el primer  numero: ");
scanf("%d",&b);
printf("Ingrese el segundo numero: ");
scanf("%d",&c);
r=b-c;
printf("El resultado es %d",r);
break;
case 3:
printf("Ingrese el primer numero: ");
scanf("%d",&b);
printf("Ingrese el segundo numero: ");
scanf("%d",&c);
r=b*c;
printf("El resultado es %d",r);
break;
case 4:
printf("Ingrese el primer numero: ");
scanf("%d",&b);
printf("Ingrese el segundo numero: ");
scanf("%d",&c);
r=b/c;
printf("El resultado es %d",r);
break;
case 5:
printf("Ingrese el primer numero: ");
scanf("%d",&b);
printf("Ingrese el numero de la potencia: ");
scanf("%d",&c);
d=1;
g=b;
e=1;
for(int i=d;i<=c;i++){
e=g*e;}
printf("El resultado es %d",e);
break;
case 6:
break;
}
}
} while(a>0 && a<=5);
}

