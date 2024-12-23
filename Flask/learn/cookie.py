from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        if username is None or password is None:
            raise Exception('错误0:用户名或密码为空')
        if username == 'admin' and password == 'admin':
            # 登录成功，创建用户身份
            response = make_response(jsonify({'msg': '登录成功,登录用户为admin'}))
            # 设置Cookie
            response.set_cookie('username', username)
            return response
        else:
            raise Exception('错误1:用户名或密码错误')
    except Exception as e:
        return jsonify({'msg': '登录失败', 'error': str(e)})
    

if __name__ == '__main__':
    app.run(debug=True)