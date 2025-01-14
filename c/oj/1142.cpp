#include<bits/stdc++.h>
using namespace std;
using ll = long  long;
const ll t = 1e9;
ll n,m,a,b,sum = 0,sum1 = 0;
ll quick_pow(ll n,ll m){
    ll res = 1,i = 0;
    while(m){
        if(m&1)res = res*n%(a+b);
        n = n*n%(a+b);
        m>>=1;
    }
    return res;
}
int main(){
    cin >> n >> m >> a >> b;
    sum = quick_pow(n,m);
    cout << sum << endl;

    return 0;
}