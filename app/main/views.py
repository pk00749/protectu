from flask import render_template, redirect, url_for, make_response
from . import main
import os


@main.route('/', methods=['GET', 'POST'])
@main.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')  # send_file('home.html')


# @main.route('/<path>')
# def today(path):
#     base_dir = os.path.join(os.path.dirname(__file__), 'videos')
#     print(base_dir)
#     resp = make_response(open(os.path.join(base_dir, path)).read())
#     resp.headers["Content-type"] = "application/json;charset=UTF-8"
#     return resp





