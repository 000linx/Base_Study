#include<bits/stdc++.h>
using namespace std;
vector<int>arr;
int n,k,sum=0,cnt=0;
int shu(int d){
    if(d<2)return 0;
    for(int i=2;i*i<=d;i++){
        if(d%i==0)return 0;
    }
    return 1;
}
void xuan(int a,int cnt,int c){
    if(a==k){
        if(shu(cnt)==1)
        sum++;
    return ;
    }
    for(int i=c;i<n;i++){
        xuan(a+1,cnt+arr[i],i+1);
    }
    return ;
}
int main(){
    cin>>n>>k;
    for(int i=1;i<=n;i++){
        int x;
        cin>>x;
        arr.push_back(x);
    }
    xuan(0,0,0);
    cout<<sum;
    return 0;
}