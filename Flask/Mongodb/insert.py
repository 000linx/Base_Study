#导入flsk和MongClient类
from flask import Flask
from pymongo import MongoClient

#创建一个flask应用
app = Flask(__name__)
#实例化MongoClient并指定了连接的地址
client = MongoClient('mongodb://localhost:27017/')
#选择了数据库
db = client['Pet_Hospital']
#选择了user这个集合,如果数据库中没有这个集合那么会自动创建
collection = db['user']

#插入
@app.route('/insert')
def insert_data():
    user = {'name': 'linx', 'age': '20', 'sex': '男', 'id': 123456}
    collection.insert_one(user)
    return "插入成功"

if __name__ == '__main__':
    app.run()