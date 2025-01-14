#include<bits/stdc++.h>
using namespace std;
int n,q,a,b,arr[1001000];
int main(){
    cin>>n>>q;
    for(int i=0;i<n;i++){
        cin>>a;
        arr[i]=a;
    }
    sort(arr,arr+n);
    for(int i=0;i<q;i++){
        int cnt=0,j=0;
        cin>>b;
        while(b>=arr[j]&&j<n){
            b-=arr[j];
            cnt++;
            j++;
        }
        cout<<cnt<<endl;
    }
    return 0;
}