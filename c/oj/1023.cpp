#include<bits/stdc++.h>
using namespace std;
int arr[1010];
int main(){
    int n,temp=0;
    cin>>n;
    for(int i=0;i<n;i++){
        int b;
        cin>>b;
        arr[i]=b;
    }
    for(int j=0;j<n;j++){
        int m=floor(sqrt(arr[j])+0.5);
        if(m*m!=arr[j]){
           if(temp<arr[j]){
            temp=arr[j];
           }

        }
    }
    cout<<temp;
    return 0;
}