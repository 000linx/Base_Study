#include<bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    ll sum = 0;
    int n,flag = 0;
    cin >> n;
    for(int i = 0 ;i < n ;i++){
        int t;
        cin >> t;
        sum+=t;
        if(sum >= 175)flag = 1;
    }
    if(flag == 1)cout << sum;
    else cout << -1;
    return 0;
}