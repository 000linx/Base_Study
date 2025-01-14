#include<bits/stdc++.h>
using namespace std;
vector<int>arr;
int ans=0,k;
void quick_sort(int l,int r){
    if(l >= r){
        return;
    }
    int i=l,j=r,flag=arr[(i+j)/2],temp;
    do{
        while(arr[i]<flag)i++;
        while(arr[j]>flag)j--;
        if(i<=j){
            temp=arr[i];arr[i]=arr[j];arr[j]=temp;
            i++,j--;
        }

    }while(i<=j);

    if(l<j)quick_sort(l,j);
    if(r>i)quick_sort(i,r);
}
int main(){
    int a;
    cin>>a;
    for(int m=0;m<a;m++){
        int temp;
        cin>>temp;
        arr.push_back(temp);
    }
    quick_sort(0,a -1);
    for(int m=0;m<a;m++){
        cout<<arr[m]<<' ';
    }
    return 0;
}