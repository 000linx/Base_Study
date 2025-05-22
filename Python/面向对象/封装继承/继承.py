#继承的优点：可以减少重复的代码
'''
继承语法 
class 子类名(父类名):
    pass
扩展父类的方法：
1.父类名.方法(self)
2.super().父类方法名()
'''

class Father(object):
    def __init__(self):
        self.money = 1000000
    def song(self):
        print('父类的歌唱天赋')
    def dance(self):
        print('父类的跳舞天赋')
    def run(self):
        print('父类的跑步天赋')
        
class Son(Father):#子类继承父类，单继承
    def song(self):#重写父类中的song方法
        print('子类的唱歌天赋')
    def dance(self):
        print('子类的跳舞天赋')
        Father.dance(self)#调用父类的方法，也是扩展父类的一种方式
    def run(self):
        print('子类的跑步天赋')
        super().run()#调用父类的方法，也是扩展父类的一种方式

#实例化子类的对象
s = Son()
#调用父类中的属性和方法
print(f'继承自父类中的钱:{s.money}')
s.song()
s.dance()
s.run()