#include <stdio.h>
int main(){
int a;
printf("Métale el numero:");
scanf("%d%*c",&a);
while(a<0){
printf("Métale un numero positivo:");
scanf("%d",&a);
}
return 0;
}
