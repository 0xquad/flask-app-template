#!/usr/bin/env python


import sys
from flask import Flask, url_for
from flaskext.genshi import Genshi, render_template


app = Flask(__name__)
genshi = Genshi(app)


def render(template, **kwargs):
    kwargs.update({
        'static' : lambda res: url_for('static', filename=res)
    })
    return render_template(template, kwargs)


def is_debug():
    return len(sys.argv) > 1 and sys.argv[1].lower() == 'debug'


@app.route('/')
def home():
    return render('home.html')



app.run(debug=is_debug())
