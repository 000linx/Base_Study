#include<bits/stdc++.h>
#define ll long long
#define endl '\n' 
using namespace std;
int n,m;
struct student{
    int t,num;
}st[1010];

bool cmp(student x , student y)
{
    if(x.t == y.t)return x.num<y.num;
    else return x.t < y.t;
} 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0),cout.tie(0);
    cin >> n;
    for(int i = 1; i <= n ; i++){
      cin >> st[i].t;
      st[i].num = i;
    }
    sort(st+1,st+n+1,cmp);
    ll sum = 0.0;
    for(int i = 1; i<= n; i++){
        cout << st[i].num << " ";
        sum += st[i].t*(n-i);
    }
    cout << endl;
    cout << setprecision(2) <<fixed<< 1.0*sum/n;
    return 0;
}