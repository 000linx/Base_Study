#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,c,d,temp=3;
    cin>>a>>b>>c>>d;
    if(a+b+temp==14 && b+c+temp==14 && c+d+temp==14 )
    cout<<"Y";
    else cout<<"N";
    return 0;
}