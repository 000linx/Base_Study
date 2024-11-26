from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Pet_Hospital']
collection = db['users']

@app.route('/updata')
def updata():
    query = {'name' : 'linx'}
    new_data = {'$set': {'age' : 18}}
    collection.update_one(query,new_data)
    return "更新成功"

if __name__ == '__main__':
    app.run()