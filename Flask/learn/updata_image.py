# 导入所需的 Flask 模块和其他库
from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import time
from datetime import timedelta

# 定义允许上传的图片文件格式
allowed_extensions = set(['png', 'jpg', 'PNG'])

# 文件格式校验函数：检查文件名是否包含点，并且扩展名在允许的列表中
def alloed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions

# 创建 Flask 应用实例
app = Flask(__name__)
# 设置响应的最大缓存时间
app.send_file_max_age_default = timedelta(seconds=1)

# 定义处理文件上传的路由
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # 从请求中获取上传的文件
        f = request.files['file']

        # 检查文件是否存在及其格式是否合法
        if not (f and alloed_file(f.filename)):
            return jsonify({'erro': 1001, "msg": "请传入正确的图片格式"})
        
        # 获取用户输入的名称
        user_input = request.form.get('name')

        # 获取当前文件的目录
        basepath = os.path.dirname(__file__)

        # 生成文件保存的路径，并安全地处理文件名
        upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))
        # 保存上传的文件
        f.save(upload_path)

        # 使用 OpenCV 读取上传的图片
        img = cv2.imread(upload_path)
        # 将读取的图像保存为 'test.jpg'
        cv2.imwrite(os.path.join(basepath, 'static/images', 'test.jpg'), img)

        # 渲染上传成功的页面，传递用户输入的名称和当前时间戳
        return render_template('upload_ok.html', User_Input=user_input, vall=time.time())

    # 如果请求方法为 GET，渲染上传页面
    return render_template('upload.html')

# 如果该脚本作为主程序运行，则启动 Flask 应用
if __name__ == '__main__':
    app.run('0.0.0.0', port=8987, debug=True)