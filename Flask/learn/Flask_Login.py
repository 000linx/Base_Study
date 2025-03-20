from flask import Flask,request,redirect,url_for
from Flask_Login import LoginManager,login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
login_manager = LoginManager()
login_manager.init_app(app)


class User:
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            user = User(username)
            login_user(user)
            return redirect(url_for('/'))
        else:
            return 'Invalid username or password'
    return  '111'