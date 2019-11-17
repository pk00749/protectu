from flask import Blueprint
admin = Blueprint('admin', __name__)


@admin.route('/admin/hello')
def hello():
    return "Welcome to protect U!"


@admin.route('/admin/login')
def login():
    return "Admin login"
