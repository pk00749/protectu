from flask import Flask
from config import DevelopmentConfig
from .main import main as main_blueprint
from .admin import admin as admin_blueprint


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(main_blueprint)
app.register_blueprint(admin_blueprint)
