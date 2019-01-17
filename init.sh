#!/bin/bash
#
# Copyright (c) 2017, Alexandre Hamelin <alexandre.hamelin gmail.com>
#
# Initializes the project virtualenv by installing requirements.

set -e

[[ "$1" = "-h" ]] && {
    echo "usage: $0 projectname  (first time execution)"
    echo "       $0  (to reinitialize the virtualenv)"
    exit
}

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

# placeholder for later
appname=myapp

[[ -d app.tmpl ]] && {
    # Check for first time execution to initialize project files.
    appname=$1
    [[ -z "$appname" || "$appname" =~ [^a-zA-Z0-9_] ]] && {
        echo "error: invalid project name '$appname' (must be alphanum only)"
        exit 1
    }
    mv app.tmpl "$appname"
    # Replace placeholders for the real project name
    sed -i -e "s/{{PROJECTNAME}}/$appname/g" $(grep -rl '{{PROJECTNAME}}' --exclude ${0##*/})
}

virtualenv -p python3 .
. bin/activate
pip install -r requirements.txt
rm -fr pip-selfcheck.json $(find -name __pycache__)

cat <<E


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Initialization done. Here are your next steps:
- Activate the virtualenv: . bin/activate
- Define your views in $appname/views.py (@app.route defs)
- Define your models in $appname/models.py (sqlalchemy models)
- Initialize the database: python -c 'from $appname import db; db.create_all()'
- Run the application:
    env FLASK_APP=$appname FLASK_ENV=development flask run -h ::
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

E
