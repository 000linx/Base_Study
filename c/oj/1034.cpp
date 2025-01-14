#include<bits/stdc++.h>
using namespace std;
int main(){
    queue<int>q;
    int m;
    string s;
    cin>>s;
    if(s=="PUSH"){cin>>m;
    q.push(m);
    while(!q.empty()){
        string m;
        if(cin>>m){
        int n;
        if(m=="PUSH"){
            cin>>n;
            q.push(n);
        }
        else if(m=="POP"){
            q.pop();
        }
        else if(m=="TOP"){
            if(!q.empty()){
            cout<<q.front()<<endl;

            }
        }
        }
        else break;
    }
    if(q.empty())cout<<"E"<<endl;
    }
    if(s=="TOP")cout<<"E";
    return 0;
}