#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//递归求阶乘
long long f(int n){
   if(n == 1)
       return 1;
    else
        return f(n - 1) * n;
}

//递归求1到100的和
long long r(int n){
    if(n == 1)
        return 1;
    else
        return r(n - 1) + n;
}

int cnt = 0;
//汉诺塔问题
void hanoi(int dish, char x, char y, char z){
    if(dish == 1){
        //当a上只剩一个盘子的时候直接从a移动到c
        printf("将%c柱的盘子移到%c柱上\n",x,z);
        cnt++;
    }
    else{
        //先将A柱子上的n - 1个盘子借助于C移动到B
        hanoi(dish - 1, x, z, y);
        printf("将%c柱的盘子移到%c柱上\n", x, z);
        cnt++;
        //再将B柱子上的n - 1盘子借助于A移动到C
        hanoi(dish - 1, y, x, z);
    }
}
int main(){
    // printf("%d\n", f(5));
    // printf("%d\n", r(100));


    hanoi(64,'A','B','C');
    printf("%d", cnt);
} 