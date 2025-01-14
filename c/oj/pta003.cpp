#include<iostream>
#include<cstring>
using namespace std;
int main(){
    int arr[10]={0};
    char num[1010];
    cin>>num;
    int n=strlen(num);
    for(int i=0;i<n;i++){
        int a=num[i]-'0';
        arr[a]++;
    }
    for(int j=0;j<=9;j++){
        if(arr[j]!=0)
        cout<<j<<":"<<arr[j]<<endl;
    }
    return 0;
}