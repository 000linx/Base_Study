#include<bits/stdc++.h>

using namespace std;
stack<int>a;
int main(){
    string s;
    cin>>s;
    int temp=0;
    for(int i = 0; i < s.length(); i++){
        int x,y;
        if(s[i]>=48 && s[i]<=57){
            temp=temp*10+s[i]-48;
        }
        else if(s[i]=='.'){
            a.push(temp);
            temp=0;
            }
        else if(s[i]=='+'){
             x=a.top();a.pop();y=a.top();a.pop();
            temp=x+y;
            a.push(temp);temp=0;
        }
        else if(s[i]=='-'){
             x=a.top();a.pop();y=a.top();a.pop();
             temp=y-x;
             a.push(temp);temp=0;

        }
        else if(s[i]=='*'){
             x=a.top();a.pop(); y=a.top();a.pop();
             temp=x*y;
            a.push(temp);temp=0;
        }
        else if(s[i]=='/'){
             x=a.top();a.pop();y=a.top();a.pop();
             temp=y/x;
             a.push(temp);temp=0;
        }
    }
    cout<<a.top();
    return 0;
}