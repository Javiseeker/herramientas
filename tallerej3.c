#include <stdio.h>
int main(){
int c;
char a,b;
printf("Primera letra:");
scanf(" %c",&a);
printf("Segunda letra:");
scanf(" %c",&b);
if(a>b)
for(c=b;c<=a;c++)
printf("%c",c);
else
for(c=a;c<=b;c++)
printf("%c",c);
return 0;
}
