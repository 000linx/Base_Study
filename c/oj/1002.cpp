#include<stdio.h>
int main(){
    int t,n;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%d",&n);
        if(n%4==0 && n%100!=0){
            printf("Yes\n");
        }
        else{printf("No\n");}
    }
    return 0;
}