#include <stdio.h>
int main(){
    int val,n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    scanf("%d",&val);
    //双指针 left左指针，right右指针
    int left = 0;
    for(int right=0;right<n;right++){
        if(arr[right]!=val){
            arr[left]=arr[right];
            left++;
        }
    }
    printf("%d",left);
    return 0;

}
