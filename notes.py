from flask import current_app, Blueprint, render_template, abort, request, flash, redirect, url_for, jsonify
from flask_login import current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required
from jinja2 import TemplateNotFound

import models
from libs.User import run_server
import random, string

notes_app = Blueprint('notes_app', __name__, template_folder='templates')

@notes_app.route('/')
def index():
    templateData = {
        'notes': models.Note.objects.order_by('-last_updated')
    }
    return render_template('index.html', **templateData)

