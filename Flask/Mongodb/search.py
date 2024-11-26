#导入flsk和MongClient类
from flask import Flask
from pymongo import MongoClient

#创建一个flask应用
app = Flask(__name__)
#实例化MongoClient并指定了连接的地址
client = MongoClient('mongodb://localhost:27017/')
#选择了数据库
db = client['Pet_Hospital']
collection = db['user']

#查询
@app.route('/query')
def query_data():
    users = collection.find()
    result = ''
    for user in users:
        result += f"Name : {user['name']}, Age : {user['age']}"
    return result

if __name__ == '__main__':
    app.run()