#include <stdio.h>
int suma(int a, int b);
int resta(int a, int b);
int potencia(int a, int b);
int factorial(int numData);
int suma2(int x, int y);
int multiplicacion(int a, int b);
int main (){
int n1, n2, a,resultado;
do{
printf("Escoja la opcion que necesite:\n 1. Suma\n 2. Resta\n 3. Multiplicación\n 4. Potencia\n 5. Factorial (NA segundo numero)\n");
scanf("%d",&a);
printf("Escoja el primer numero: ");
scanf("%d",&n1);
printf("Escoja el segundo numero: ");
scanf("%d",&n2);
if(a<=0 || a>5){
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
case 4:
resultado=potencia(n1,n2);
printf("%d",resultado);
printf("\n");
break;
case 5:
resultado=factorial(n1);
printf("%d",resultado);
printf("\n");
break;
}}
}
while(a>0 && a<=5);
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
int potencia(int a, int b){
int r=a;
int c=0;
for(int i=0;i<b;i++){
r=r+c;
c=0;
for(int h=1;h<a;h++){
c=c+r;
}
}
return r;
}
int suma2(int x, int y){
int cont1=x;
int total=0;
int temp=y;
if(cont1==1){
return y;
}
else{
while(cont1!=0){
total=total+temp;
cont1=cont1-1;
}
return total;
}
}
int factorial(int numData){
int var=numData;
int flag=var-1;
int total=0;
while(flag!=0){
total=suma2(flag,var);
flag=flag-1;
var=total;
}
return var;
}
