#include <bits/stdc++.h>
using namespace std;
int cnt=0,sum=0,arr[100010],i,j;
int main(){
    int n;
    cin>>n;
    for(i=2;i<=n;i++){
        for(j=2;j<=sqrt(i);j++){
            if(i%j==0)break;
        }
        if(j>sqrt(i)){
            arr[cnt]=i;//储存素数
            cnt++;//统计素数个数
        }
    }
    for(int i=0;i<=cnt;i++){
        if(arr[i+1]-arr[i]==2)sum++;//判断相邻素数之差是否为2
    }
    cout<<sum;
    return 0;
}
