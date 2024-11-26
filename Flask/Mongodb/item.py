from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Pet_Hospital']
collection = db['users']

@app.route('/insert')
def insert_data():
    user = {'account':'111222','pwd':'13456dasdqw','name':'linx','age':18}
    user1 = {'account':'111222','pwd':'13456dasdqw','name':'zhx','age':18}
    collection.insert_one(user)
    collection.insert_one(user1)
    return 'success'

@app.route('/search')
def search_data():
    users = collection.find()
    result = ''
    for user in users:
        result += f"name:{user['name']}<br>"
    return result

@app.route('/updata')
def updata_information():
    query = {'name':'linx'}
    new_data = {'$set': {'age':20}}
    collection.update_one(query,new_data)
    return 'success'

@app.route('/delete')
def delete_data():
    query = {'name':'zhx'}
    collection.delete_one(query)
    return 'success'

if __name__ == '__main__':
    app.run()
