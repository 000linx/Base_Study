#flask蓝图
from flask import Blueprint
#创建蓝图对象，并设置蓝图名称为wx_login和wx_logout
wx_login_blueprint = Blueprint('wx_login',__name__)
wx_logout_blueprint = Blueprint('wx_logout',__name__)
#定义路由和视图函数，并设置路由前缀分别为/wx_login和/wx_logout
@wx_login_blueprint.route('/login')
def login():
    return 'login success'
@wx_logout_blueprint.route('/logout')
def logout():
    return 'logout success'