#导入flsk和MongClient类
from flask import Flask
from pymongo import MongoClient

#创建一个flask应用
app = Flask(__name__)
#实例化MongoClient并指定了连接的地址
client = MongoClient('mongodb://localhost:27017/')
#选择了数据库
db = client['Pet_Hospital']

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()