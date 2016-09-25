#include <stdio.h>
int suma(int a, int b);
int resta(int a, int b);
int multiplicacion(int a, int b);
int main (){
int n1, n2, a,resultado;
do{
printf("Escoja la opcion que necesite:\n 1. Suma\n 2. Resta\n 3. Multiplicación\n");
scanf("%d",&a);
printf("Escoja el primer numero: ");
scanf("%d",&n1);
printf("Escoja el segundo numero: ");
scanf("%d",&n2);
if(a<=0 || a>3){
printf("valor incorrecto");
}
else{
switch(a)
{
case 1:
 resultado=suma(n1,n2);
printf("%d",resultado);
printf("\n");
break;
case 2:
resultado=resta(n1,n2);
printf("%d",resultado);
printf("\n");
break;
case 3:
resultado=multiplicacion(n1,n2);
printf("%d",resultado);
printf("\n");
break;
}}
}
while(a>0 && a<=3);
}
int suma(int a, int b){
return a+b;
}
int resta(int a, int b){
return a-b;
}
int multiplicacion(int a, int b){
int r=0;
for(int i=1;i<=b;i++){
    r=r+a;
}
return r; 
}
