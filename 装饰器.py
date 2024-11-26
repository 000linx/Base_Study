#装饰器本质是一个闭包函数，装饰器的返回值也是一个函数对象
#它可以在其他函数不需要做任何代码变动的前提下增加额外的功能
'''
装饰器模板
装饰器的本质：把真正要执行的业务函数的函数名作为参数传到装饰器中
def wrapper(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs) #真正要执行的业务函数
        return res
    return inner
'''
#无参数修饰器
def wrapper(func):
    def inner():
        print("这是inner")
        func()
    return inner
#真正的业务函数
def test():
    print("这是方法一")
#法一：把真正要执行的业务函数的函数名作为参数传到装饰器中
t1 = wrapper(test)
t1()#这一步是调用，不写这一步代表的是闭包
#法二：语法糖@
@wrapper#通过语法糖让test1与wraooer产生关系
def test1():
    print("这是方法二")
test1()#此时业务函数可以像普通的函数一样调用

#有参数的装饰器
def logger(func):
    def wrapper(a,b):
        print("准备调用{}".format(func.__name__))
        func(a,b)
        print("计算完成")
    return wrapper


#法一同上
def add(a,b):
    print(f'{a} + {b} = {a + b}')
t3 = logger(add)
t3(1,5)

#法二
@logger
def add1(a,b):
    print(f'{a} + {b} = {a + b}')
add1(2,3)