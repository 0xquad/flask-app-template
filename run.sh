#!/bin/sh
. bin/activate
export FLASK_APP=${FLASK_APP:-$(echo */__init__.py)} FLASK_ENV=${FLASK_ENV:-development}
exec flask run -h ::
