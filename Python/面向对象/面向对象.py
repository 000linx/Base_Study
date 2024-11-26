#面向过程：更加看重开发的步骤和过程
#面向对象：更加重开发的对象和对象之间的关系

#类的定义
# 类名：大驼峰命名法
# 类名后面的括号是继承的意思，object是python中的基类，所有类都继承自object
#写法
#class Studetn(object):或者class Student:
class Student(object):
    pass

#类的实例化
#对象名 = 类名()
s1 = Student()
print(id(s1))
s2 = Student()
print(id(s2))