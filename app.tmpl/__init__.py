# Main application file
#
# Copyright (c) 2020, Alexandre Hamelin <alexandre.hamelin gmail.com>


import os
from flask import Flask

app = Flask(__name__)

with app.app_context():
    app.config.from_object(app.name + '.config.DefaultConfig')
    if 'APP_CONFIG' in os.environ:
        app.config.from_envvar('APP_CONFIG')

    from .views import app_bp
    from .models import *
    app.register_blueprint(app_bp, url_prefix=app.config.get('APP_URL_ROOT', '/'))
    app.secret_key = 'default-secret-key'
