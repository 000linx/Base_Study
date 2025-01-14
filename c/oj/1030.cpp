#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int arr[101];
    for(int i=0;i<n;i++){
        arr[i]=1;   
    }
    int sum=0,x=n;
    for(int i=0; ;i=(i+1)%x){
         if(arr[i]==1)sum++;
        else continue;
        if(sum==m){
            cout<<i+1<<" ";
            arr[i]=0;
            sum=0;
            n--;
        }
        if(n==0)break;
    }
   return 0;
   }