#include <bits/stdc++.h>
using namespace std;
vector<int>arr;
char shu(int a){
    switch(a){
        case 0:cout<<"ling";
        break;
         case 1:cout<<"yi";
        break;
         case 2:cout<<"er";
        break;
         case 3:cout<<"san";
        break;
         case 4:cout<<"si";
        break;
         case 5:cout<<"wu";
        break;
         case 6:cout<<"liu";
        break;
         case 7:cout<<"qi";
        break;
         case 8:cout<<"ba";
        break;
         case 9:cout<<"jiu";
        break;
    }
    return 0;
}
int main(){
    char num[101];
    int sum=0,cnt=0,flag=0;
    cin>>num;
    int n=strlen(num);
    for(int j=0;j<n;j++){
        int a=num[j]-'0';
        sum+=a;
    }
    while(sum>0){
        int x=sum%10;
        arr.push_back(x);
        sum/=10;
        cnt++;
    }
    int m=cnt;
    while(cnt>0){
        if(m==cnt){
            shu(arr[cnt-1]);
        }
        else {
            printf(" ");
            shu(arr[cnt-1]);
        }
        cnt--;
    }
return 0;
}