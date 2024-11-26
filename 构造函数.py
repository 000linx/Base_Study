#__init__方法：在实例化对象时自动调用，用来初始化对象的属性
#类属性和实例属性
#类属性：类中，所有方法外的变量称为类属性，被该类的所有对象所共享
#实例属性：类中，方法内部以“self.属性名”的方式定义的变量称为实例属性，只能被对象本身调用，对象之间的实例属性互不影响

#实例属性的调用优先级高于类属性
#类属性的调用：类名.类属性 或者 对象.类属性

class User(object):
    count = 0 #count就是类属性，被该类的所有对象所共享
    def __init__(self,name,age,sex,id,phone): #在实例化对象时会自动调用该方法，用来初始化对象的属性
        self.name = name #self.name就是实例属性，name就是参数，self就是对象本身
        self.age = age
        self.sex = sex
        self.id = id
        self.phone = phone
        User.count += 1 #类属性的调用：类名.类属性 或者 对象.类属性

    def show_info(self):
        print(f'姓名：{self.name},年龄：{self.age},性别：{self.sex},身份证号：{self.id},手机号：{self.phone}')
print(f'此时类中的user个数为{User.count}') #0
#实例化对象，将对象的属性赋值给对象
linx = User('linx',18,'男','123456789012345678','13812345678') #此时的User中的self就是linx
linx.show_info()
print(f'此时类中的user个数为{User.count}')
lily = User('lily',18,'女','123456789012345678','13812345678') #此时的User中的self就是lily
lily.show_info()
print(f'此时类中的user个数为{User.count}')

#实例属性的调用优先级高于类属性
#类属性的调用：类名.类属性 或者 对象.类属性
#实例属性的调用：对象.实例属性