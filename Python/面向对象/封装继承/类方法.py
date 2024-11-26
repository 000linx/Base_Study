#类方法：在类中定义的方法，使用@classmethod装饰器进行修饰，第一个参数是cls，代表类本身，而不是类的实例。
'''
class 类名:
    @classmethod
    def 方法名(cls,参数列表):
        方法体
'''
#静态方法：在类中定义的方法，使用@staticmethod装饰器进行修饰，没有特殊的参数要求。
'''
class 类名:
    @staticmethod
    def 方法名(参数列表):
        方法体
'''

class Preson:
    num = 100
    @classmethod
    def say_hello(cls):#cls是形参，实参是Preson
        print('hello')
    @staticmethod
    def say_world():
        print('world')
    @classmethod
    def update_num(cls):
        Preson.num += 1

p = Preson()
#实例对象调用类方法
p.say_hello()
p.update_num()
print(Preson.num)