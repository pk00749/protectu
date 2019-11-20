from flask import render_template, redirect, url_for
from . import main


@main.route('/', methods=['GET', 'POST'])
@main.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')  # send_file('home.html')



