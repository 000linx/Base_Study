#include<bits/stdc++.h>
#define ll long long 
#define endl '\n'
#define L(a,b,c) for(int a = b ;i < c ; i++) 
using namespace std;

int n,a,b,l = 1e7, r =0;
int sum = 0;
struct t{
int star,end;
};
bool cmp(t x, t y){
   return x.star < y.star;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0),cout.tie(0);
    cin >> n;
    vector<t>vec;
    L(i,0,n){
        cin >> a >> b;
        vec.push_back({a,b});
    }
    sort(vec.begin(),vec.end(),cmp);
    for(int i = 0 ;i < vec.size() ;i++){
        if(vec[i].star >= r){
            r = vec[i].end;
            sum++;
        }
    }
    cout << sum;


    return 0;
}
