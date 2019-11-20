from flask import render_template
from . import main


@main.route('/admin',methods=['GET','POST'])
def admin():
    return '''Hello admin!
            <a href="/logout" style="color: red">退出</a>
        '''


@main.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')

