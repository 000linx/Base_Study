#include<bits/stdc++.h>
using namespace std;
int fx(int a){
    if(a==0)return 0;
    else if(a==1)return 1;
    else return fx(a-1)+fx(a-2);
}
int sx(int b){
    int sum=0;
    if(b<10){
        sum=b;
        return sum;
        }
    while(b>0){
        int a=b%10;
        sum+=a;
        b/=10;
    }
    return sum;
}
int main(){
    int n,m;
    cin>>n;
    for(int i=0;i<n;i++){
        int cnt=0;
        cin>>m;
        for(int t=1;t<=m;t++){
         int k=fx(t);
         int j=sx(k);
         cnt+=j;
        }
        cnt=cnt%9;
    cout<<cnt<<endl;
    }
    return 0;
}