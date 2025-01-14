#include <stdio.h>
int main()
{
    double n;
    int s;
    scanf("%lf %d",&n,&s);
if (s>=700){
    printf ("%.2f\n",0);
}
if (s<=699&&s>=600){
    printf("%.2f\n",n*0.4);
}
if (s<=599&&s>=500){
    printf("%.2f\n",n*0.6);
}
if (s<=499&&s>=400){
    printf("%.2f\n",n*0.8);
}
if (s<400){
    printf("%.2f\n",n);
}
return 0;
}