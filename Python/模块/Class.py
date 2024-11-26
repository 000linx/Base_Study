class User(object):
    def __init__(self,name,age,sex,id,phone):
        self.name = name
        self.age = age
        self.sex = sex
        self.id = id
        self.phone = phone

    def show_info(self):
        print(f'姓名：{self.name},年龄：{self.age},性别：{self.sex},身份证号：{self.id},手机号：{self.phone}')
linx = User('linx',18,'男','123456789012345678','13812345678')
linx.show_info()