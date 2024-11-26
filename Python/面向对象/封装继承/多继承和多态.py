#多继承：一个子类继承多个父类
#多态：一个事物有多种形态
#多态性：可以定义统一的接口，传入不同的对象，得到不同的结果
class Father ():
    def dance(self):
        print('父亲的跳舞天赋')
    def money(self):
        print('父亲的钱')
class Mother():
    def sing(self):
        print('母亲的唱歌天赋')
    def money(self):
        print('母亲的钱')
class Son(Father,Mother):#多继承，一个子类继承多个父类
    def money(self):
        print('儿子的钱')
s = Son()
f = Father()
m = Mother()
#多态，定义一个统一的接口
def func(obj):
    obj.money()
func(s)
func(m)
func(f)
s.dance()
s.sing()
#继承的多个父类中有相同的方法，执行的是第一个继承的父类中的方法
s.money() #父亲的钱
