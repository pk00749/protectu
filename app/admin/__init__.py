from flask import Blueprint

#: 初始化Main蓝图. 注意静态文件和模板文件夹路径
#: 模板路径是 root_path + template_folder
#: root_path 是 blueprintdemo的路径
admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates')

# must be at the end, otherwise pop up error "cannot import name 'main' from 'app.main'", don't know why
from . import views
