#!/bin/sh
. bin/activate
export FLASK_APP=${FLASK_APP:-$(dirname $(echo */__init__.py))} FLASK_ENV=${FLASK_ENV:-development}
exec flask run -h :: "$@"
