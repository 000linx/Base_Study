from flask import Flask,Blueprint
#从blueprint中导入蓝图对象blue
from blueprint import blue
app = Flask(__name__)

#注册蓝图对象
'''
有两个参数，第一个参数是蓝图对象，第二个参数是url前缀
如果不写url前缀，默认是/，写了之后访问的路径是/url前缀/路由，即是/test/index
app.register_blueprint(blue,url_prefix='/test')
'''
app.register_blueprint(blue)

if __name__ == '__main__':
    app.run(debug=True)
