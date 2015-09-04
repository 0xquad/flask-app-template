# Application models
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>


import os, os.path
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from {{PROJECTNAME}} import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
    os.path.join(app.root_path, app.name + '.db'))

db = SQLAlchemy(app)


#class MyClass(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    # Quickref:
#    # types: Integer, String, Text, DateTime, ForeignKey
#    # keywords: primary_key, nullable, unique, default
#    # rels: backref=db.backref('ModelName')
#
#
#    def __init__(self, ...):
#        pass
#
#
#    def __str__(self):
#        return self.name
#
#
#    def __repr__(self):
#        return '<{} {!r}>'.format(self.__class__.__name__, self.id)
