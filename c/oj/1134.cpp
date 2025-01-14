#include<bits/stdc++.h>
using namespace std;
int n,m,k,l;//n对弈数，m英雄数，k血量，l金币数
int r1,c1,r2,c2,r3,c3;//自己英雄的r1费用，c1阶数;r2,c2为对手的
pair<int,int>arr[100],arr1[100],arr2[100];
int quan1[100],quan2[100],quan3[100];
int sum1=0,sum2=0,jmin=0,smax=0;
void add1(int x,int y){
    sum1+=x+y-1;
}
void add2(int x,int y){
    sum2+=x+y-1;
}
void pvp(int a,int b){
    if(a>b){
        l+=10;
    }
    else{
        k-=(b-a)*2;
        l+=2;
    }
}
void shang(int c){
    if(c==1){
        l+=arr[jmin].second;
        for(int i=0;i<5;i++){
            cin>>r3>>c3;
            arr2[i].first=r3;
            arr2[i].second=c3;
            quan3[i]=arr2[i].first+arr2[i].second-1;
            if(l>=arr2[i].second){
            if(quan3[i]>quan3[smax]){
                smax=i;
            }
        }
    }
    l-=arr2[smax].second;
    sum1+=quan3[smax]-quan1[jmin];
    quan1[jmin]=quan3[smax];
    pvp(sum1,sum2);
    }
    else {
        l-=4;
        cin>>arr[m].first>>arr[m].second;
        quan1[m]=arr[m].first+arr[m].second-1;
        if(quan1[jmin]>quan1[m]){
            jmin=m;
        }
        sum1+=quan1[m];

        pvp(sum1,sum2);
    }
}
int main(){
    cin>>n>>m>>k>>l;
    for(int i=0;i<m;i++){
        cin>>r1>>c1;
        add1(r1,c1);
        arr[i].first=r1;
        arr[i].second=c1;
        quan1[i]=arr[i].first+arr[i].second-1;
        if(quan1[i]<quan1[jmin]){
            jmin=i;
        }
    }
    for(int i=0;i<n;i++){
        int z,s;
        sum2=0;
        cin>>z;
       for(int j=0;j<z;j++){
        cin>>r2>>c2;
        add2(r2,c2);
        arr1[j].first=r2;
        arr1[j].second=c2;
        quan2[j]=arr1[j].first+arr1[j].second-1;
       }
       cin>>s;
       shang(s);
    }
    if(k<=0)cout<<"wuwu";
       else cout<<k;
       return 0;
}