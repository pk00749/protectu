from flask import Flask, render_template
from flask_pymongo import PyMongo
from admin import admin
from config import DevelopmentConfig
from operate import operate
import re

app = Flask(__name__)
app.register_blueprint(admin)
app.register_blueprint(operate)
app.config.from_object(DevelopmentConfig)
print(app.config.get('ENV'))
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('login.html')  # send_file('index.html')


@app.route('/login')
def login():
    for res in mongo.db.info.find({'created_by': re.compile("")}):
        print(res['created_by'])
    return str(mongo.db.info.find_one()['db_created_date'])


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='localhost')


