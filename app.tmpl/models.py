# Application models
#
# Copyright (c) 2016, Alexandre Hamelin <alexandre.hamelin gmail.com>


import os, os.path
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from {{PROJECTNAME}} import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
    os.path.join(app.root_path, app.name + '.db'))

db = SQLAlchemy(app)
migrate = Migrate(app, db)


#class MyModel(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    # Quickref:
#    # types: Integer, String(L), Text, DateTime, ForeignKey('table.col')
#    # keywords: primary_key, nullable, unique, default
#    # rels: db.relationship('OtherModel', backref=db.backref('mymodels'))
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
