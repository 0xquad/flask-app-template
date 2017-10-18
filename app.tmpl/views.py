# Application views
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>


from flask import request, url_for, jsonify, redirect, abort
from flaskext.genshi import Genshi, render_template
from flask_login import login_user, logout_user, login_required, current_user
from {{PROJECTNAME}} import app
from {{PROJECTNAME}}.models import *


genshi = Genshi(app)
genshi.extensions['html'] = 'html5'



def render(template, **kwargs):
    """Render a Genshi template with some extra helpers."""
    kwargs.update({
        'static' : lambda res: url_for('static', filename=res)
    })
    return render_template(template, kwargs)



@app.route('/')
def home():
    """Display homepage"""
    return render('home.html')


