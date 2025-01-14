#include<bits/stdc++.h>
using namespace std;
const int M=50001;
int a[M],b[M],c[M];
int main(){
    string s1,s2;
    cin>>s1>>s2;
    
    for(int i=0;i<s1.length();i++){
        a[i]=s1[s1.length()-1-i]-'0';
    }
    for(int i=0;i<s2.length();i++){
        b[i]=s2[s2.length()-1-i]-'0';
    }
    for(int i=0;i<50001;i++){
        c[i]+=a[i]+b[i];
        c[i+1]+=c[i]/10;
        c[i]%=10;
    }
    int flag=0;
    for(int i=50001;i>=0;i--){
        if(c[i]!=0)flag=1;
        if(flag==1)cout<<c[i];
    }
    if(flag==0)cout<<c[0];
    return 0;
}