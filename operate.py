from flask import Blueprint

operate = Blueprint('operate', __name__)


@operate.route('/operate/hello')
def index():
    return "index"


@operate.route('/operate/login')
def login():
    return "login"

