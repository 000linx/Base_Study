<<<<<<< HEAD
#字符串用一对双引号或一对单引号来定义一个字符串
a = 10
print(a,type(a))    #10 <class 'int'>
b = '10'
print(b,type(b))    #10 <class 'str'>
#输出的结果相同，但是数值的类型是不同的

#字符串的操作
# + 拼接
a = 'Hello'
b = '408'
print(a + ' ' + b)

# *复制
a = '111'
print(a * 3)

# in/ not in 判断是否在字符串中返回bool值
a = 'Hello World'
print('e' in a )    #True
print('h' in b )    #False

#格式化输出
#1.占位符 %
age = 20
name = 'linx'
print('我的姓名是：%s,年龄是：%d'%(name,age))

str = 'abcde'
print('%10s'%(str))     #    abcde占十位向右对齐
print('%-10s!'%(str))   #abcde     !占十位向左对齐
print('%.2s'%(str))     #ab截取前面两位

number = 12.455
print('%.2f'%(number))  #%.2f表示保留两位小数，默认是保留六位

#format-----先占位，后填坑
print('{},{}'.format('linx',12))
number = 12.4111
print('{:.2f}'.format(number))  #保留两位小数

#f表达式
print(f'我的姓名是{name},我的年龄是{age}')
=======
#字符串用一对双引号或一对单引号来定义一个字符串
a = 10
print(a,type(a))    #10 <class 'int'>
b = '10'
print(b,type(b))    #10 <class 'str'>
#输出的结果相同，但是数值的类型是不同的

#字符串的操作
# + 拼接
a = 'Hello'
b = '408'
print(a + ' ' + b)

# *复制
a = '111'
print(a * 3)

# in/ not in 判断是否在字符串中返回bool值
a = 'Hello World'
print('e' in a )    #True
print('h' in b )    #False

#格式化输出
#1.占位符 %
age = 20
name = 'linx'
print('我的姓名是：%s,年龄是：%d'%(name,age))

str = 'abcde'
print('%10s'%(str))     #    abcde占十位向右对齐
print('%-10s!'%(str))   #abcde     !占十位向左对齐
print('%.2s'%(str))     #ab截取前面两位

number = 12.455
print('%.2f'%(number))  #%.2f表示保留两位小数，默认是保留六位

#format-----先占位，后填坑
print('{},{}'.format('linx',12))
number = 12.4111
print('{:.2f}'.format(number))  #保留两位小数

#f表达式
print(f'我的姓名是{name},我的年龄是{age}')
>>>>>>> 5169a62fdb26c2a597b35a0bc9f27034826ef6de
