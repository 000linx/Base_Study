#include<bits/stdc++.h>
using namespace std;
int main(){
    int l,n,cnt=-1;
    cin>>l>>n;
    char arr[l];
    int sum=pow(26,l)-n;
    for(int i=0;i<l;i++){
        arr[i]=sum%26+'a';
        cnt++;
        sum/=26;
    }
    while(cnt>=0){
        cout<<arr[cnt];
        cnt--;
    }
    return 0;
}