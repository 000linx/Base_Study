# 最简单的登录操作
# 导入基本的库
from flask import Flask, request, jsonify
# 创建Flask应用
app = Flask(__name__)

#登录路由实现
@app.route('/login', methods=['POST'])
def login():
    # 用try expect捕获异常
    try:
        # 从请求中获取用户名和密码
        data = request.get_json()
        username = data['username']
        password = data['password']
        # 判断获取到的值是否为空
        if username is None or password is None:
            raise Exception('错误0:用户名或密码为空') # 抛出异常
        # 在这里进行实际的登录验证，这里假设用户名和密码都为'admin'
        if username == 'admin' and password == 'admin':
            return jsonify({'msg': '登录成功,登录用户为admin'}),200
        else:
            raise Exception('错误1:用户名或密码错误')
    except Exception as e:
        return jsonify({'msg': '登录失败', 'error': str(e)}) 

if __name__ == '__main__':
    app.run(port=4000)