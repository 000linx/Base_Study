#include<bits/stdc++.h>
using namespace std;
int cnt=0;
int com(int n){
    int temp1=0,temp2=0,a=n,b=n;
    while(a>0){
        temp1+=a%10;
        a/=10;
    }
    for(int i=0;b>0;i++){
        temp2+=b%2;
        b/=2;
    }
    if(n>=1){
        if(temp1==temp2){
            cnt++;
            return com(n-=1);
        }
        else com(n-=1);
    }
    return cnt;
}
int main(){
    int n;
    cin>>n;
    cout<<com(n);
    return 0;
}