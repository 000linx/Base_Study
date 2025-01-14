#include<bits/stdc++.h>
using namespace std;
int arr1[10],arr2[10];
void xu(int n){
    if(n!=6174){
        int i=0,a=0,b=0;
    while(n>0){
        arr1[i]=n%10;
        arr2[i]=n%10;
        n/=10;
        i++;
    }
    sort(arr1,arr1+4);
    sort(arr2,arr2+4,greater<int>());
    for(int i=0;i<4;i++){
        a=a*10+arr1[i]*10;
        b=b*10+arr2[i]*10;  
    }
    a/=10;
    b/=10;
    if(arr1[0]==0){
        if(b-a!=6174){
            cout<<b<<" - 0"<<a<<" = "<<b-a<<endl;
            return xu(b-a);
        }
        else cout<<b<<" - 0"<<a<<" = "<<6174;
    }
    else {
        if(b-a!=6174){
            cout<<b<<" - "<<a<<" = "<<b-a<<endl;
            return xu(b-a);
        }
        else cout<<b<<" - "<<a<<" = "<<6174;

    }
    }
}
int main(){
    int n;
    cin>>n;
    if(n%1111==0){
        cout<<n<<" - "<<n<<" = "<<"0000";
    }
    else xu(n);

    return 0;
}