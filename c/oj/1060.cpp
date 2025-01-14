#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m,sum=0,cnt=0;
    cin>>n>>m;
    while(n>0){
        sum++;
        n--;
        cnt++;
        if(cnt==m){
            n++;
            cnt-=m;
        }
    }
    cout<<sum;
    return 0;
}