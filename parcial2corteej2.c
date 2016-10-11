#include <stdio.h>
int main(){
float area, constante=2, radio2, circunferencia, diametro, radio, pi=3.1416;
printf("Ingrese el radio del circulo: ");
scanf("%f",&radio);
diametro= radio*constante;
circunferencia= diametro*pi;
radio2=radio*radio;
area= pi*radio2;
printf("circunferencia: %f",circunferencia);
printf("diametro: %f",diametro);
printf("area: %f",area);
}
