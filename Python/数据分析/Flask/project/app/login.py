from flask import Flask, jsonify, request
from pymongo import MongoClient
from utils import *
import redis

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['project']

@app.route('/account_login', methods = ['POST'])
def login():
    try:
        data = request.get_json()
        account = data['account']
        password = data['password']
        if account and password:
            if account == 'admin' and password == 'admin01234':
                
                raise jsonify({'message': 'Login successful'})
        else:
            raise jsonify({'message': 'Invalid credentials'})
    except Exception as e:
        return jsonify({'message': str(e)})


@app.route('/verity_code_login', methods = ['POST'])
def login():
    try:
        data = request.get_json()
        phone = data['phone']
        code = data['code']
        if phone and code:
            r = redis.Redis(host='localhost', port=6379, db=0)
            stored_code = r.get(phone)
            if stored_code == code:
                raise jsonify({'message': 'Login successful'})
            else:
                raise jsonify({'message': 'Invalid code'})
    except Exception as e:
        return jsonify({'message': str(e)})


@app.route('/send_code', methods = ['GET'])
def send_verity_code():
    try:
        phone = request.args.get('phone')
        if phone:
            code = generate_code()
            send_code(code, phone)
            r = redis.Redis(host='localhost', port=6379, db=0)
            r.set(phone, code, ex=600)
            raise jsonify({'message': 'Code sent successfully'})
        else:
            raise jsonify({'message': 'Invalid phone number'})
    except Exception as e:
        return jsonify({'message': str(e)})
