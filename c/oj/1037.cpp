#include <bits/stdc++.h>
using namespace std;
int main(){
    string s,s1;
    getline(cin,s);
    getline(cin,s1);
    for(int i=0;i<s1.length();i++){
        for(int j=0;j<s.length();j++){
            if(s1[i]==s[j]){
                s.erase(j--,1);
            }
        }
    }
    cout<<s;
    return 0;
}