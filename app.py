#!/usr/bin/env python


from flask import Flask, url_for, request
from flaskext.genshi import Genshi, render_template


app = Flask(__name__)
genshi = Genshi(app)
genshi.extensions['html'] = 'html5'


def render(template, **kwargs):
    kwargs.update({
        'static' : lambda res: url_for('static', filename=res)
    })
    return render_template(template, kwargs)


def run_app(app):
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-d', '--debug', dest='debug', default=False,
                      action='store_true',
                      help='Turn on debugging')
    parser.add_option('-p', '--port', dest='port', type=int, default=5000,
                      help='Specify the server port')
    parser.add_option('-l', '--listen', dest='listen_addr', default='::1',
                      help='Specify the listening address')
    options, args = parser.parse_args()
    app.run(host=options.listen_addr, port=options.port, debug=options.debug)



@app.route('/')
def home():
    return render('home.html')



run_app(app)
