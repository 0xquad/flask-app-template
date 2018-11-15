# Application models
#
# Copyright (c) 2018, Alexandre Hamelin <alexandre.hamelin gmail.com>


import os, os.path
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import column_property
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from {{PROJECTNAME}} import app, login_manager


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI',
    'sqlite:///{}'.format(os.path.join(os.path.dirname(app.root_path), app.name + '.db')))
# or e.g. DB_URI=mysql+pymysql://user:pass@server/dbname

db = SQLAlchemy(app)
migrate = Migrate(app, db)

__all__ = (
    'db',
)


# Quickref:
# types: Integer, String(L), Text, DateTime, ForeignKey('table_name.col')
# keywords: primary_key, nullable, unique, default
# rels: db.relationship('OtherModel', backref=db.backref('mymodels'), lazy='dynamic'))
# other_id = db.Column(db.Integer, db.ForeignKey('othermodel.id'))

#class MyModel(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
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
