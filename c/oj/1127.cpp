#include<bits/stdc++.h>
#define ll long long
#define endl '\n'
using namespace std;
const int N = 100100;
ll m;
int n,t;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0),cout.tie(0);
    cin >> n;
    int a[N],b[N];
    for(int i = 1 ;i <= n ; i++){
        cin >> a[i];
    }
    sort(a+1,a+1+n);
    int sum = 0;
    for(int i = 1; i  <= n ; i++){
        b[i] = b[i-1] + a[i];
        sum++;
    }
    bool ok = false;
    int l = 1 ,r = n -1 ;
    while( l <= r){
        
    }
    if(ok)cout << "YES";
    else cout << "NO";
    return 0;
}