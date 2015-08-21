#!/bin/bash

set -e

virtualenv -p python3 .
. bin/activate
pip install -r requirements.txt
sed -i 's/\.iteritems/.items/g' lib/*/site-packages/flaskext/genshi.py
rm -f $0
