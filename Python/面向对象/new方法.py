#__new__()才是实例化对象时调用的第一个方法，它只接受一个cls参数
'''
两个作用
1.在内存中为对象分配空间
2.返回对象的引用，将引用作为第一个参数，传递给__init__()方法
'''
class A(object):
    def __init__(self):
        print("这是init")
    def __new__(cls):
        print("这是new中的cls：",cls)
        #返回对象的引用，本质是扩展父类，因为object是所有基类的父类
        return object.__new__(cls) #创建对象
        #return supre().__new__(cls)
a = A()
print(a)

class B(object):
    def __new__(cls):
        print("这是new中的cls：",cls)
        new_B = object.__new__(cls) #创建对象，为其分配空间，0x7a66b10ef0e0
        print("这是new中的new_B对象：",new_B)
        return new_B
    def __init__(self): 
        print("这是init中的self:",self) #0x7a66b10ef0e0，验证对象传参b传给了self

print(B)
b = B()
print("这是b对象:",b) #0x7a66b10ef0e0，与new_B相同，说明对象b是由new_B创建的