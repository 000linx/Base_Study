#类：具有相同属性和方法的对象的集合
#对象：类的实例化
#属性：对象的属性，名词，和变量几乎一样
#方法：对象的行为，动词，和函数几乎一样，只是方法定义在类中且第一个参数必须是self，代表对象本身
class  Preson(object):
        pass

#实例化对象并且单独给对象赋值
preson = Preson()
preson.name = 'linx'
preson.age = 20
print(f'{preson.name}的年龄是{preson.age}')


class  A:
        def test(self):
                print('test')
#通过对象获取方法
a = A()
a.test()

class B:
        def test(self):
                print(f'{self.name}的年龄是{self.age}')
#在方法内通过self获取对象属性
b = B()
b.name = 'linx'
b.age = 20
b.test()