#include<stdio.h>
int main(){
    int n;
    int a,b,c;
    scanf("%d",&n);
    a=n/100;
    b=n/10%10;
    c=n%10;
    if(a!=0){
        for(int i=0;i<a;i++){
            printf("B");

        }
    }
    if(b!=0){
        for(int i=0;i<b;i++){
            printf("S");
        }
    }
    if(c!=0){
        for(int i=1;i<=c;i++){
            printf("%d",i);
        }
    }

    return 0;
}