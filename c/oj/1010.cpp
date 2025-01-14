#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,arr[1000];
    int cnt=0;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    sort(arr,arr+n);
    int a[1000],b=0,c=0;
    a[0]=arr[0];
    while(b<n){
        if(arr[b]!=arr[++c]){
            b=c;
        }
        else cnt++;
    }
    cout<<n-cnt<<endl;
    int x=unique(arr,arr+n)-arr;
    for(int i=0;i<x;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}