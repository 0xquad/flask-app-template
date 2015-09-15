#!/bin/bash
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>
#
# Initializes the project virtualenv by installing requirements.

set -e

[[ -e requirements.txt ]] || {
    echo 'not in the project directory? missing requirements.txt'
    exit 1
}

[[ -z "$VIRTUAL_ENV" ]] || {
    echo 'already in a virtualenv'
    exit 1
}

[[ -d bin ]] && [[ -d lib ]] && [[ -d include ]] && {
    echo 'virtualenv already initialized'
    exit 1
}

appname=$1
[[ -z "$appname" || "$appname" =~ [^a-zA-Z0-9_] ]] && {
    echo "invalid project name '$appname' (must be alphanum only)"
    exit 1
}

mv app.tmpl "$appname"
virtualenv -p python3 .
. bin/activate
pip install -r requirements.txt
# Fix for Python 3
sed -i -e 's/\.iteritems/.items/g' lib/*/site-packages/flaskext/genshi.py
# Replace placeholders for the real project name
sed -i -e "s/{{PROJECTNAME}}/$appname/g" $(grep -rl '{{PROJECTNAME}}' --exclude $0)

cat <<E

Initialization done. Here are your next steps:
- Define your views in $appname/views.py (@app.route defs)
- Define your models in $appname/models.py (sqlalchemy models)
- Initialize the database: python -c 'from $appname import db; db.create_all()'

E
