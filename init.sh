#!/bin/bash

set -e

virtualenv -p python3 .
. bin/activate
pip install -r requirements.txt
rm -f $0
