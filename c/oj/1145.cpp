#include<bits/stdc++.h>
using namespace std;
using ll = long long;
ll a[10010],b[10010];
int main(){
    int n;
    cin >> n;
    for(int i = 0 ;i < n ; i++)
    {   
        cin >> a[i];
        b[i] = a[i];
    }
    sort(a,a+n);
    for(int i = 0 ;i < n ;i++){
        if(b[i] == a[n-1])b[i] = b[i] + a[n - 2];
        else b[i] = b[i] + a[n - 1];
        cout << b[i] << " ";
    }
}