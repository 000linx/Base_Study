from flask import Flask
from flask import redirect,render_template,request

app = Flask(__name__)

# 定义路由'/login'，只接受GET请求
@app.route('/login', methods=['GET'])
def login():
    # 如果请求方法是GET，渲染并返回登录页面模板
    if request.method == 'GET':
        return render_template('/login.html')
    # 从表单中获取用户名和密码
    username = request.form.get('user')
    pwd = request.form.get('pwd')
    print(username,pwd)

    # 如果用户名和密码正确则重定向到index路由
    if username == 'linx' and pwd == 'hello 408':
        return redirect('index')
    else :
    #  如果错误则返回到登录页面并返回报错信息
        return render_template('/login.html', msg = '账号或密码错误')
# 定义index路由，它接受GET和 POST的请求    
@app.route('/index', method = ['GET','POST'])
def index():
    return {"user" : 'linx', "stats" : 'success'} 

if __name__ == '__main__':
    app.run()