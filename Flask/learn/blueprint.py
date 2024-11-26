#flask 蓝图工具
from flask import Flask,Blueprint

#创建蓝图对象，第一个参数是蓝图的名称，第二个参数是所在的模块
blue = Blueprint('blue',__name__)

#在蓝图中定义路由
@blue.route('/index')
def index():
    return 'index'
