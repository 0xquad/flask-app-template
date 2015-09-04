# Main application file
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>


from flask import Flask
app = Flask(__name__)

# Import anything that depended on `app`
from {{PROJECTNAME}}.views import *
from {{PROJECTNAME}}.models import *
