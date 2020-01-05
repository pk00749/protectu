from flask import *
from pymongo import MongoClient
import re
from datetime import timedelta
from config import DevelopmentConfig

client = MongoClient(host='localhost', port=27017)
db = client['protectu']

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config["SECRET_KEY"] = "nothingissecretknow?"

@app.route("/user/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("/user/login.html")
    else:
        username = request.form["username"]
        password = request.form['password']
        valid_username = db.users.find_one({"username": username})
        session['userlogged'] = True
        return redirect(url_for('home'))


@app.route('/user/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('/user/register.html')
    else:
        username = request.form["username"]
        password = request.form['password']
        try:
            userDet = {'username': username, 'password': password}
            res = db.users.insert(userDet)
            if res:
                return redirect(url_for("login"))
            else:
                render_template('/user/register.html')
        except:
            return redirect(url_for('home'))

@app.route('/home')
def home():
    username = 'york'
    return render_template('/user/login.html', username=username)

@app.route('/user/logout')
def logout():
    session.pop('userlogged')
    return redirect('/home')


if __name__ == '__main__':
    app.run()
