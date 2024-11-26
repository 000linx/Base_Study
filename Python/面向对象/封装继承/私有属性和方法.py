#私有属性和方法
'''
1._x 单前置下划线，私有属性或方法，属于伪私有，只能在类的内部使用，不能通过from xxx import * 导入，能通过对象名访问，子类可以访问
2.__xx 双前置下划线，私有属性或方法，属于私有，只能在类的内部使用，不能通过from xxx import * 导入，也不能通过对象名访问，子类不可以访问
3.__xx__ 双前后下划线，系统定义的特殊方法或属性，如__init__(),__str__(),__del__(),__dict__()等，子类不可以访问

'''
class User():
    name = "linx"
    _age = 18
    __sex = "男"
    def get_sex(self):
        return self.__sex
    #修改私有属性的值
    def set_sex(self,new_sex):
        self.__sex = new_sex
c = User()
print(c.name)
print(c._age)
#无法直接访问
#print(c.__sex)#'User' object has no attribute '__sex'
#强行获取私有属性，对象名._类名__私有属性名
print(c._User__sex)
print(c.get_sex())
c.set_sex("女")
print(c.get_sex())

#私有属性或方法访问---在公有方法中调用私有属性或方法
# 定义一个名为 Classmate 的类
class Classmate():
    # 定义一个私有属性 __name，其值为 "linx"
    __name = "linx"
    # 定义一个私有方法 __Privet，该方法会打印 "私有方法"
    def __Privet(self):
        print("私有方法")
    # 定义一个公有方法 Public
    def Public(self):
        # 打印私有属性 __name 的值
        print(self.__name)
        # 打印 "公有方法"
        print("公有方法")
        # 调用私有方法
        # 注意：在公有方法中调用私有方法，需要使用 self.__方法名() 的形式
        self.__Privet()

c = Classmate()
c.Public()