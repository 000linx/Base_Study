# jwt身份认证
from flask import request, jsonify, Flask
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'test'

# 登录路由实现
@app.route('/jwt_login', methods=['POST'])
def login():
    try:
        # 从请求中获取用户名和密码
        data = request.get_json()
        username = data['username']
        password = data['password']
        # 判断获取到的值是否为空
        if username is None or password is None:
            raise Exception('错误0:用户名或密码为空')
        # 在这里进行实际的登录验证，这里假设用户名和密码都为'admin'
        if username == 'admin' and password == 'admin':
            # 用用户名作为鉴权字段生成JWT令牌
            access_token = create_access_token(identity=username)
            return jsonify({'msg': '登录成功', 'access_token': access_token})
        else:
            raise Exception('错误1:用户名或密码错误')
    except Exception as e:
        return jsonify({'msg': '登录失败', 'error': str(e)})

# 受保护的路由实现
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    try:
        # 从JWT令牌中获取当前登录的用户名
        current_user = get_jwt_identity()
        if current_user is None:
            raise Exception('错误0:未登录')
        # 在这里进行实际的访问验证，这里假设只有登录用户为'admin'的用户才能访问
        if current_user == 'admin':
            return jsonify({'msg': '访问成功', 'current_user': current_user})
        else:
            raise Exception('错误1:无权限')
    except Exception as e:
        return jsonify({'msg': '访问失败', 'error': str(e)})
if __name__ == '__main__':
    app.run(port = 4000)
