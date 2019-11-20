from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def admin():
    return '''Hello main!
            <a href="/logout" style="color: red">退出</a>
        '''


@main.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# @app.route('/')
# def index():
#     return render_template('login.html')  # send_file('index.html')
#
#
# @app.route('/login')
# def login():
#     for res in mongo.db.info.find({'created_by': re.compile("")}):
#         print(res['created_by'])
#     return str(mongo.db.info.find_one()['db_created_date'])
