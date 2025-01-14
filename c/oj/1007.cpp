#include<bits/stdc++.h>
using namespace std;
int main(){
    long long n,sum=0,temp,temp1;
    cin>>n;
    for(int i=0;i<10001;i++){
        sum++;
        temp=n;
        long long a=0,b=0;
        while(temp!=0){
            a=a*10+temp%10;
            temp/=10;
        }
        if(n==a){break;}
        n=a+n;
        temp1=n;
        while(temp1!=0){
            b=b*10+temp1%10;
            temp1/=10;
        }
        if(n==b){break;}
        if(sum>1000){
            sum=-1;
            break;
        }
    }
    cout<<sum;
    return 0;

}