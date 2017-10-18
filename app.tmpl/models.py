# Application models
#
# Copyright (c) 2017, Alexandre Hamelin <alexandre.hamelin gmail.com>


import os, os.path
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import column_property
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from {{PROJECTNAME}} import app, login_manager


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///{}'.format(os.path.join(app.root_path, app.name + '.db'))
#   'mysql+pymysql://root@{}/{}'.format(os.environ['DB_SERVER', 'localhost'], app.name)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

__all__ = (
    'db',
)


# Quickref:
# types: Integer, String(L), Text, DateTime, ForeignKey('table_name.col')
# keywords: primary_key, nullable, unique, default
# rels: db.relationship('OtherModel', backref=db.backref('mymodels'))
class ID(db.Column):
    def __init__(self, *args, **kwargs):
        kwargs.pop('primary_key', None)
        super().__init__(db.Integer, primary_key=True, *args, **kwargs)


class Int(db.Column):
    def __init__(self, *args, **kwargs):
        kwargs.pop('nullable', None)
        super().__init__(db.Integer, nullable=False, *args, **kwargs)

#class MyModel(db.Model):
#    id = ID()
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
