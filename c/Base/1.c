
#include <stdio.h>

int main(){

printf("hell0 408");
/*
1.基本数据类型
整型 (int): 用于存储整数。一般占用4个字节（32位），具体大小依赖于系统。 

short: 通常占用2个字节。
long: 通常占用4个字节或8个字节，取决于系统。%
long long: 至少占用8个字节。
字符型 (char): 用于存储单个字符，占用1个字节。

unsigned char: 只存储非负字符。
signed char: 可以存储负字符。
浮点型 (float): 用于存储单精度浮点数，通常占用4个字节。

双精度浮点型 (double): 用于存储双精度浮点数，通常占用8个字节。

长双精度浮点型 (long double): 精度更高，通常占用8字节或16字节，具体取决于实现。

常用的是int %d, long %ld, float %f, double %lf, long long %lld, char %c
*/
//用法
int a;
char b;
long c;
float d;
double e;
long long f;


/*
2.输入输出函数
格式化
scanf输入函数，是stdio库中所包含的基本函数
printf输出函数
*/
printf("hello,408");//printf会在终端打印" "里面的东西
printf("请输入一个整数");
scanf("%d",&a);
printf("%d\n",a);

printf("请输入一个字符");
scanf("%c",&c);
printf("%c\n",c);

/*
3.运算符
算术运算符
+：加法
-：减法
*：乘法
/：除法
%：取余（模运算）

关系运算符
用于比较两个值，返回布尔值（真或假）。
==：等于
!=：不等于
>：大于
<：小于
>=：大于等于
<=：小于等于

逻辑运算符
&&：逻辑与（AND）
||：逻辑或（OR）
!：逻辑非（NOT）

自增自减运算符
++：自增（可以放在变量前后）
--：自减（可以放在变量前后）
*/

int t1 = 20, t2 = 30;
printf("%d\n",t2 % t1);//取余是取两数相除所得的余数
printf("t1 == t2: %d\n", t1 == t2);  // 0 (false)
printf("t1 != t2: %d\n", t1 != t2);  // 1 (true)
printf("t1 > t2: %d\n", t1 > t2); //0(false)

int n = 10 , m , q;
m = n++;
printf("m的值是: %d\n",m);
printf("n的值是: %d\n",n);
q = ++n;
printf("q的值是: %d\n",q);

/*
条件判断语句 if ,if else, if else if
*/
int t = 10;
if(t > 10){
    printf("t > 10\n");
} else {
    printf("t < 10\n");
}

if(t > 0){
    printf("t是正数\n");
} else if{
    printf("t是负数\n");
} else {
    printf("t为0\n");
}

//条件判断
int result = t > 1 ? 1 : 0;

    return 0;
}