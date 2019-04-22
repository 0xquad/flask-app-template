# Application views
#
# Copyright (c) 2019, Alexandre Hamelin <alexandre.hamelin gmail.com>


from flask import request, url_for, jsonify, redirect, abort, current_app, session
from flask_genshi import Genshi, render_template
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import literal, text, and_, or_
from sqlalchemy.sql import literal
from sqlalchemy.orm.exc import NoResultFound
from . import app
from .models import *


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


def validate_user_login(user_id, passwd):
    profile = UserProfile.query.filter_by(email_addr=user_id).first()
    validated = profile and profile.check_password(passwd)
    if validated:
        login_user(profile)
    return validated


def check_safe_url(url):
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = None
    error = None
    if request.method == 'POST':
        email = request.form.get('email', None)
        password = request.form.get('password', None)

        if validate_user_login(email, password):
            # the 'next' parameter is automatically added to the URL
            # when the user accesses a route with @login_required while
            # not authenticated
            next_url = request.args.get('next', '')
            #check_safe_url(next_url)
            if not next_url.startswith('/'):
                next_url = None
            return redirect(next_url or url_for('home'))
        else:
            error = 'Invalid credentials.'

    return render('login.html', email=email, error=error)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
