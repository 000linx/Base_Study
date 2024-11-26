#析构函数
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("初始化对象{0}".format(self.name))
    def __del__(self):#如果希望在对象被销毁前再做一些事情，可以考虑一下__del__方法，主要是销毁/删除临时变量
        print("销毁对象{0}".format(self.name))

p = Person("张三",18)
print("1")
print("2")
print("3")

#使用del 删除对象时，会自动调用__del__方法，相当于手动释放内存