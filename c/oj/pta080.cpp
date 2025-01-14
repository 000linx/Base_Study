#include <bits/stdc++.h>
#include<vector>
using namespace std;
vector<int>arr;
void xiangc(int a,int b){
    int n=a*b;
        if(n<10){
        arr.push_back(n);
    }
    else{
            int x1=n/10;
            int x2=n%10;
            arr.push_back(x1);
            arr.push_back(x2);
    }
}
int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    arr.push_back(a);
    arr.push_back(b);
    for(int j=0;j<c;j++){
        xiangc(arr[j],arr[j+1]);
    }
    for(int i=0;i<c;i++){
      if(i==0){
        cout<<arr[i];
      }
      else cout<<" "<<arr[i];
}
    return 0;
}