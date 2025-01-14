#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    cin>>n;
    for(int i=0;i<n;i++){
        int sum=0,cnt=0;
        string s;
        cin>>m;
        for(int i=0;i<m;i++){
            char c;
            cin>>c;
            int g=s.find(c);
            if(g==-1)sum+=2;
            else sum++;
            s+=c;
            }
        cout<<sum<<endl;
    }
    return 0;
}