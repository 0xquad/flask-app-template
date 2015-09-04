# Application views
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>


from flask import request, url_for, jsonify
from flaskext.genshi import Genshi, render_template
from {{PROJECTNAME}} import app, render
from {{PROJECTNAME}}.models import db


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


