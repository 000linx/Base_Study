#异常：即使语句或表达式在语法上是正确的，在运行时也有可能发生错误。运行期检测到的错误被称为异常。
#异常处理：捕捉异常并处理异常。

#异常处理的基本语法：
#try:
#    <语句>        #运行别的代码
#except <名字>：
#    <语句>        #如果在try部份引发了'name'异常
#except <名字>，<数据>:
#    <语句>        #如果引发了'name'异常，获得附加的数据
#else:
#    <语句>        #如果没有异常发生
#finally:
#    <语句>        #退出try时总会执行
#try-except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
#如果你不想在异常发生时结束你的程序，只需在try里捕获它。
#异常种类：
#ZeroDivisionError：除数为0
#NameError：尝试访问一个没有申明的变量
#SyntaxError：语法错误
#IndentationError：缩进错误
#KeyError：请求一个不存在的字典关键字
#IndexError：请求一个不存在的列表元素
#FileNotFoundError：请求一个不存在的系统文件
#TypeError：不同类型间的无效操作

# try:
#     print(a)
# except NameError as e:
#     print(e)
# print('111')
# print('222')

def test1():
    a = input('请输入密码：')
    if len(a) >= 6:
        return a
    else:
        raise Exception('密码长度不够')
    
try:
    print(test1())
except Exception as e:
    print(e)
