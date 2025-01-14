#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    cin>>n;
    int a[1010]={0};
    for(int i=0;i<n;i++){
        cin>>m;
        a[m]++;
        cout<<a[m]<<" ";
    }
    return 0;
}