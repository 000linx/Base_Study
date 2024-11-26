#python中的循环有两种while和for
num = 0
while num < 10:
    print(num)
    num += 1
#python中有while...else语句在不满足循环条件时执行else中的语句
else:
    print(num)

#for循环可以遍历任何序列的项目，如一个列表或者一个字符串
for i in 'hello 408':
    print(i)

List = [1,2,3,4]
for i in List:
    print(i)


import time

local = time.asctime(time.localtime(time.time()))
print(local)