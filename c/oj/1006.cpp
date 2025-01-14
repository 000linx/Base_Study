#include <stdio.h>
int main()
{
    int n,m,a=0,b=0,cnt=0;
    char c[5];
    scanf("%d",&n);
    for(int i=0;i<n-1;i++){
        scanf("%s",c);
        if(c[0]=='Y') a++;
        if(c[0]=='N') b++;
        else {cnt++;}
    }
    printf("%d\n",a);
if(b+1<=cnt){
    printf("TRUE");
}
else{
    printf("FALSE");
}
    return 0;
} 