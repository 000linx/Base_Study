#在python中有多种方式表达数组
'''
1.list 列表[]
2.tuple 元组()不可变数组,即无法进行增删查改
3.set 集合{}或者set()
4.dict 字典{}或者dict(),以键值对的方式存储

'''

#list可以存储任何类型的数据，并且动态的增加和删除元素
test_list = [1,2,3,4,5]
print(test_list)    #打印整个数组
print(test_list[0]) #打印数组中的第一个数

test_list[0] = 10   #修改第一个数的值

#插入元素insert(index,element),
test_list.insert(1,9)   #表示将9这个数字插入到索引为1的值的后面
print(test_list)
test_list.append(-2,7)  #负数则表示倒序插入在索引为2的前面
print(test_list)

#尾插append和extend
#两种方法的不同之处是append是将列表作为一个整体插入，而extend是将列表拆开分别插入
test_list.append([6,7,8]) #向数组末尾增加一个值
print(test_list)
test_list.extend([6,7,8]) #向数组末尾增加一个值
print(test_list)

#统计元素出现的次数count，没有则返回0,这里的元素不仅是基本的数据类型也可以是复杂数据类型
num = test_list.count(1)
print(num)

#获取数组的长度len
length = len(test_list)
print(length)

#删除元素
#del,pop,remove
del test_list[0] #删除索引为0的元素
del test_list[1:3] #删除从1到2的元素[1,3)左闭右开区间
# del test_list会删除整个列表

#pop(index)
test_list.pop() #index是可选参数用于删除指定位置的值，不写则默认删除最后一个元素

#remove(element)
test_list.remove(10) #用于删除第一次出现的元素