#封装：将属性和方法封装到一个类中，通过实例化对象来调用属性和方法
class Soldier():
    def __init__(self,name,model,num):
        self.name = name
        self.model = model
        self.num = num
    def shoot(self):
        if self.num == 0:
            print(f'{self.name}没有子弹了')
        else:
            self.num -= 1
            print(f'{self.name}发射了子弹，剩余子弹{self.num}颗')
            
s = Soldier('zs','AK47',5)
s.shoot()

#上述代码封装了Soldier类，通过实例化对象来调用属性和方法
#其中的name，model，num就是属性，shoot就是方法