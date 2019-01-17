# Main application file
#
# Copyright (c) 2019, Alexandre Hamelin <alexandre.hamelin gmail.com>


import os
from flask import Flask
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = 'default-secret-key'

app.config.from_object(app.name + '.config.DefaultConfig')
if 'APP_CONFIG' in os.environ:
    app.config.from_envvar('APP_CONFIG')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import anything that depended on `app`
from .views import *
from .models import *
