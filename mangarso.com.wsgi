#!/usr/bin/python

activate_this = '/var/www/mangarso.com/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.append('/var/www/mangarso.com')

from app import app as application