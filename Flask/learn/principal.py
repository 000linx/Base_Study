from flask import Flask, request, jsonify,session
from flask_principal import Principal, Permission, RoleNeed,Identity,identity_changed,identity_loaded

app = Flask(__name__)
# 初始化Flask-Principal
app.config['SECRET_KEY'] = 'test'
principals = Principal(app)

# 定义角色和权限
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # 从session中获取用户角色
    role = session.get('role')
    if role == 'admin':
        identity.provides.add(RoleNeed('admin'))

# 登录路由
@app.route('/principal_login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        if username is None or password is None:
            raise Exception('错误0:用户名或密码为空')
        if username == 'admin' and password == 'admin':
            session['role'] = username
            # 登录成功，创建用户身份
            identity = Identity(username)
            # 将用户身份添加到Flask-Principal中
            identity.provides.add(RoleNeed('admin'))
            identity_changed.send(app, identity=identity)
            print(identity.provides)
            return jsonify({'msg': '登录成功,登录用户为admin'})
        else:
            raise Exception('错误1:用户名或密码错误')
    except Exception as e:
        return jsonify({'msg': '登录失败', 'error': str(e)}),400
    

# 受保护的路由
@app.route('/protected', methods=['GET'])
@admin_permission.require(403)
def protected():
    return jsonify({'msg': 'admin访问成功'})

if __name__ == '__main__':
    app.run(debug=True,port=4000)