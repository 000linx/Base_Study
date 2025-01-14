#include<stdio.h>
int main(){
    int x,a[20][20];
    scanf("%d",&x);
    for(int i=0;i<x;i++){

        for(int j=0;j<=i;j++){

            if(i==j||j==0) {
                a[i][j]=1;
                }
            else{
                 a[i][j]=a[i-1][j-1]+a[i-1][j];
                }
        }
    }
        for(int i=0;i<x;i++){
            for(int j=0;j<=i;j++){
                printf("%d\x20",a[i][j]);
            }
            printf("\n");
        }
        return 0;
    }