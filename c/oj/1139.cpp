#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<algorithm>
using namespace std;
//判断长度是否相同
//判断字母是否相同}
vector<string>s;
vector<string>s1;
map<string,int>m;
string trans(string s){
    string r = s;
    for(int i = 0 ; i < r.length();i++){
        r[i] = tolower(r[i]);
    }
    sort(r.begin(),r.end());
    return r;
}
int main(){
    string n;
    while(cin >> n){
        if(n[0] == '#')break;
        s.push_back(n);
        string x = n;
        for(int i = 0; i<n.size();i++){
            x[i] = tolower(x[i]);
        }
        sort(x.begin(),x.end());
        string n1 = x;
        if(!m.count(n1))m[n1] = 0;
        m[n1]++;
    }
    
    for(int i = 0; i < s.size();i++){
        if(m[trans(s[i])] == 1)s1.push_back(s[i]);
    }
    sort(s1.begin(),s1.end());
    if(s1.empty()){
        cout << -1;
        return 0;
    }
    for(int i = 0 ; i < s1.size(); i++){
        cout << s1[i] << endl;
    }

    return 0;
}