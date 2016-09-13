#include <stdio.h>
int main(){
int a, b=0,positivos=0,negativos=0, par=0, impar=0;
for(b=0;b<10;b=b+1){
printf("Digite un numero %d:",b);
scanf("%d", &a);
if(a>0)
positivos++;
else
negativos++;
if(a%2==0)
par++;
else
impar++;
}
printf("Los numeros son %d, %d, %d, %d:",positivos,negativos,par,impar);
return 0;
}
