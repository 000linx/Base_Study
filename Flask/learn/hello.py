# 导入 Flask 类，Flask 是一个用于构建 web 应用的 Python 框架
from flask import Flask

# 创建一个 Flask 应用实例，__name__ 是当前模块的名称
app = Flask(__name__)

# 使用 @app.route('/') 装饰器定义路由，'/' 表示应用的根 URL
@app.route('/')
# 定义一个视图函数 hello，当用户访问根 URL 时，这个函数会被调用
def hello():
    # 返回字符串 "hello 408" 作为 HTTP 响应的主体
    return "hello 408"

# 检查当前脚本是否作为主程序运行
if __name__ == '__main__':
    # 如果是主程序，则调用 app.run() 启动 Flask 应用
    # 这将启动一个本地开发服务器，并在默认端口 5000 上监听请求
    app.run()