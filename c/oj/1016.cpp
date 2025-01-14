#include <bits/stdc++.h>
using namespace std;
int main(){
    int arr[10]={0};
    char num[1010];
    cin>>num;
    int n=strlen(num);
    for(int j=0;j<n;j++){
        int a=num[j]-'0';
        arr[a]++;
    }
    for(int i=0;i<=9;i++){   
        if(arr[i]!=0)                                                                         
        cout<<i<<":"<<arr[i]<<endl;
}
return 0;
}