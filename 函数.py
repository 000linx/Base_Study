#定义：将具有独立功能的代码块组织为一个整体，使其具有特殊功能的代码集

#函数结构
# def 函数名（参数）：
#     函数体
#     return 返回值

#python变量查找顺序：局部变量->全局变量->内置变量  就近原则  局部变量可以使用全局变量，全局变量不能使用局部变量

def func(a):
    print('hello')
    print(a)
    return a + 1

def funa():
    a = 1
    b = [1,2]
    c = {1,2,3}
    return a,b,c
#查看函数说明
import random
#两种方式
print(random.__doc__)
print(help(random))

#函数的调用： 函数名（参数）
func(10)

#函数的返回值：return 会把返回值返回到函数的调用处；如果返回多个值则是以元组的类型   1.返回值  2.结束函数的执行  3.返回值可以是任意数据类型
b = func(10)
print(b)
print(funa())
print(type(funa()))

#函数的参数   
# 1.位置参数：写几个就要传几个  
# 2.关键字参数 ：接受所有的关键字参数然后将其转化为一个字典，赋值给形参 
# 3.默认参数：在不传入参数时使用的默认的值  
# 4.不定长参数：将实参所有的位置参数全部接收到一个元组中

"""
def 函数名(形式参数a,形式参数b):
    函数体
    return 返回值
"""
def add(a,b):
    return a + b
print(add(1,2))

def Sex(name,sex = '男'):
    print(name,sex)
Sex('张三') #未传值时使用默认值
Sex('李四','女') #传值时使用传入的值

# 不定长参数定义 *参数名 例如：*args
def Args(*args):
    print(args)
Args(1,2,3,4,5,6) #将实参所有的位置参数全部接收到一个元组中

def Kwargs(**kwargs):
    print(kwargs)
Kwargs(a = 1,b = 2,c = 3) #将实参所有的关键字参数全部接收到一个字典中

#函数嵌套调用
#先执行的是funa，再执行funb
def funa():
    def funb():
        print('hellob')
    print('helloa')
    funb()
funa() 

#return调用函数
def funa():
    def funb():
        print('hellob')
    print('helloa')
    return funb()
funa() #先执行funa，再执行funb

#1.修改全局变量 global  2.修改局部变量 nonlocal
a = 1
def func():
    global a #将局部变量a变为全局变量,此时修改的值为2，不再是1
    a = 2
    print(a)
func()
print(a)

def funx():
    a = 1
    def funy():
        nonlocal a 
        a = 2
        print(a)
    print(a)
    funy()
funx()

#对于一些简单的函数定义可以使用匿名函数
#语法：lambda 参数1，参数2：表达式  冒号前面的是参数，冒号后面的是表达式，表达式的结果就是返回值
add = lambda x,y: x + y
print(add(1,2))