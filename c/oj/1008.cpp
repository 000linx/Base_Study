#include<bits/stdc++.h>
using namespace std;
vector<int> arr[110];//用于储存人的编号
int a[111],cnt=0,b[110]={0};
int main(){
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>a[i];//输入队伍
        a[i]*=10;//每个队伍有多少人
    }
    int cnt=0,k=1;
    while(cnt<n){
        for(int i=1;i<=n;i++){
            if(arr[i].size()<a[i]){//当队伍没有存满时
                arr[i].push_back(k);
                if(cnt==n-1)k+=2;
                else k++;
            }
            if(arr[i].size()==a[i]&&b[i]==0){//当队伍刚好存满
                cnt++;
                b[i]=1;
            }
        }
    }
    for(int i=1;i<=n;i++){
        cout<<"#"<<i<<endl;
        for(int j=0;j<arr[i].size();j++){
            if(j!=0 && (j+1)%10==0)cout<<arr[i][j]<<endl;//队尾输出并换行
            else cout<<arr[i][j]<<" ";
        }
    }
    return 0;
}

