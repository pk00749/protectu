from flask import *
from pymongo import MongoClient
import re, time
from datetime import timedelta
from config import DevelopmentConfig

client = MongoClient(host='localhost', port=27017)
db = client['protectu']

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config["SECRET_KEY"] = "nothingissecretknow?"


@app.route('/')
@app.route("/user/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("/user/login.html")
    else:
        username = request.form["username"]
        password = request.form['password']
        valid_username = db.users.find_one({"username": username})
        session['userlogged'] = True
        return redirect(url_for('user_info', username=username))


@app.route('/user/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('/user/register.html')
    else:
        username = request.form["username"]
        password = request.form['password']
        try:
            userDet = {'username': username, 'password': password, 'register_date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) }
            res = db.users.insert(userDet)
            if res:
                return redirect(url_for("login"))
            else:
                render_template('/user/register.html')
        except:
            return redirect(url_for('home'))


@app.route('/user/logout')
def logout():
    session.pop('userlogged')
    return redirect('/home')


@app.route('/home')
def home():
    # TODO: show user name
    username = 'vip'
    return render_template('/user/login.html', username=username)


@app.route('/user/insurances')
def insurances():
    username_list = []
    for u in db.users.find({}):
        username_list.append(u['username'])
    return render_template('/user/insurances.html', u=username_list)


@app.route('/user/info')
def user_info():
    userinfo = []
    for u in db.users.find({}):
        userDic = {'username':u['username'], 'register_date':u['register_date']}
        userinfo.append(userDic)
    for i in userinfo:
        print(i)
    return render_template('/user/info.html', res=userinfo)


if __name__ == '__main__':
    app.run()
