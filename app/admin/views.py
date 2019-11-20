from flask import render_template
from . import admin


# @admin.route('/admin/index', methods=['GET', 'POST'])
# def index():
#     return render_template('home.html')


@admin.route('/admin', methods=['GET', 'POST'])
def admin():
    return '''Hello admin!
            <a href="/logout" style="color: red">退出</a>
        '''


