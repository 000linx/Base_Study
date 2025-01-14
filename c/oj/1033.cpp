#include<bits/stdc++.h>

using namespace std;
stack<int>a;
int main(){
    string s;
    cin>>s;
    if(s=="TOP")
    {
        cout<<"E";
    }
    else if(s=="PUSH")
    {
        int n;
        cin>>n;
        a.push(n);
        while(!a.empty())
        {
        string m;
        if(cin>>m){
        if(m=="PUSH")
        {
            cin>>n;
            a.push(n);
        }
        if(m=="POP")
        {
            a.pop();
        }
        if(m=="TOP")
        {
            cout<<a.top()<<endl;

        }
        }
        else break;
        }
        if(a.empty())cout<<"E"<<endl;
    }
    return 0;
}