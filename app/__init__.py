from flask import Flask
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
