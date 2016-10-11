#include <stdio.h>
int sumatoria(int a, int b, int c, int d, int e);
int promedio(int a, int b, int c, int d, int e);
int main () {
int resultado1, resultado2, dato1, dato2, dato3, dato4, dato5;
printf("Ingrese los 5 datos a los que le desea sacar la sumatoria y el promedio: ");
scanf(" %d",&dato1);
printf("segundo dato: ");
scanf(" %d",&dato2);
printf("tercer dato: ");
scanf(" %d",&dato3);
printf("cuarto dato: ");
scanf(" %d",&dato4);
printf("quinto dato: ");
scanf(" %d",&dato5);
printf("El resultado de la sumatoria es: ");
resultado1=sumatoria(dato1, dato2, dato3, dato4, dato5);
printf("%d",resultado1);
printf("El resultado del promedio es: ");
resultado2=promedio(dato1, dato2, dato3, dato4, dato5);
printf("%d",resultado2);
}
int sumatoria(int a, int b, int c, int d, int e){
return a+b+c+d+e;
}
int promedio(int a, int b, int c, int d, int e){
return (a+b+c+d+e)/5;
}
