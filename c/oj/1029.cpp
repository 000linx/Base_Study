#include<bits/stdc++.h>

using namespace std;

int a[101]={0},b[101]={0},c[101];
int main(){
    int n,m;
    cin>>n>>m;
    for(int i=n-1;i>=0;i--){
        cin>>a[i];
    }
    for(int i=m-1;i>=0;i--){
        cin>>b[i];
    }
    int temp=max(n-1,m-1);
    for(int i=temp;i>=0;i--)
        c[i]=a[i]+b[i];

    for(int i=temp;i>=0;i--)
        cout<<c[i]<<" ";
    return 0;
}