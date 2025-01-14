#include<bits/stdc++.h>
#define ll long long 
#define endl '\n'
using namespace std;

bool cmp(pair<int,int> a,pair<int,int> b){
    if(a.second!=b.second) return a.second>b.second;
    else return a.first<b.first;
}

int main(){
    int n;
    cin >> n;
    map<int,int> mp;
    for(int i=0;i<n;i++){
        int num;
        cin >> num;
        if(!mp.count(num))
            mp[num] = 0;
        mp[num]++;
    }
    vector<pair<int,int>> vec(mp.begin(),mp.end());
    sort(vec.begin(),vec.end(),cmp);
    for(int i=0;i<vec.size();i++){
        cout << vec[i].first << " " << vec[i].second << endl;
    }
    return 0;
}