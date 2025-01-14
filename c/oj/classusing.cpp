#include<stdio.h>
int main()
{
  int a,b,c,sum=0,cnt=0;
  for(int i=999;i>=100;i--){
   a=i/100;
   b=(i-a*100)/10;
   c=i%10;
   if(cnt==3)break;
    if(i==a*a*a+b*b*b+c*c*c){
      printf("%d\n",i);
      sum+=i;
      cnt++; 
  }

  }
  printf("%d",sum);
    return 0;
    }