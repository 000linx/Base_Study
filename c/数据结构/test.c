#include <stdio.h>
int main(){
    int target,n;
    scanf("%d",&n);
    scanf("%d",&target);
    int arr[10] = {2,7,11,5};
    for (int i = 0; i < 4 ;i++){
        int b = target - arr[i];
        for(int j = i + 1; j < 4 ;j++){
            if(b == arr[j]){
                printf("%d,%d",i,j);
                return;
            }
        }
    }
    return 0;
}