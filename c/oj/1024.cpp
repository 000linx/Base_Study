#include<bits/stdc++.h>
using namespace std;
queue<int>qx,qy;
//记录马是否到过这个位置
int a[410][410];
//记录马到一个位置的步数
int step[410][410];
//记录马走日字的八个方向
int dx[8]={1,1,-1,-1,2,2,-2,-2};
int dy[8]={-2,2,-2,2,1,-1,1,-1};
struct point{
    int x,y;
}node;
queue<point>q;
int main(){
    //清空数组，并且全部赋值为-1
    memset(step,-1,sizeof(step));
    int n,m,x,y;
    cin>>n>>m>>x>>y;
    //用队列存储初始的起点
    node.x = x;
    node.y = y;
    q.push(node);
    //初始的那一个位置步数为0
    step[x][y]=0;
    //初始的位置记录为1代表这个位置已经走过了
    a[x][y]=1;
    while(!q.empty()){//当这个队列不是空的时候开始循环
    for(int i=0;i<8;i++){//遍历八个方向
    //下一步的位置为当前的位置加上马走的方向
        int nextx=q.front().x+dx[i];
        int nexty=q.front().y+dy[i];
        if(nextx>0 && nexty>0 && nextx<=n && nexty<=m && a[nextx][nexty]==false){//判断这个位置是不是走过的
            a[nextx][nexty]=true;//将走过的位置记录为真
            step[nextx][nexty]=step[q.front().x][q.front().y]+1;//到这个位置的步数加一
            //将该位置存入队列
           node.x = nextx;
           node.y = nexty;
           q.push(node);

        }
    }
    //将上一个位置拿出队列
    q.pop();
}
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            printf("%-5d",step[i][j]);
        }
        cout<<endl;
    }
    return 0;
}