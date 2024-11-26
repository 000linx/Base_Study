#模块
'''
1.内置库
2.第三方库
3.自定义库

导入模块
1.import 模块名称
'''
import utils
from flask import Flask
from route import wx_login_blueprint,wx_logout_blueprint
print(utils.add(1,2))
# 查看模块的路径
print(utils.__file__)
app = Flask(__name__)
#注册蓝图，并设置蓝图的前缀分别为/wx_login和/wx_logout
app.register_blueprint(wx_login_blueprint,url_prefix = '/wx_login')
app.register_blueprint(wx_logout_blueprint,url_prefix = '/wx_logout')

#py文件的两种功能
#脚本：一个文件就是整个程序，被用来执行
#模块：一个文件就是一个模块，被其他文件导入



if __name__ == '__main__':#当做脚本直接运行时，__name__的值为__main__
    app.run()
