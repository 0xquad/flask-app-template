# Main application file
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>


from flask import Flask
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = 'default-secret-key'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import anything that depended on `app`
from {{PROJECTNAME}}.views import *
from {{PROJECTNAME}}.models import *
