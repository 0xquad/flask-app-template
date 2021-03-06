# Application models
#
# Copyright (c) 2020, Alexandre Hamelin <alexandre.hamelin gmail.com>


import os, os.path
from sqlalchemy import select
from sqlalchemy.orm import column_property
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI',
    'sqlite:///{}'.format(os.path.join(os.path.dirname(app.root_path), app.name + '.db')))
# or e.g. DB_URI=mysql+pymysql://user:pass@server/dbname

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = f'{app.name}.login'


__all__ = (
    'db',
    'UserAccount',
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


class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    @property
    def is_active(self): return True
    @property
    def is_authenticated(self): return True
    def get_id(self, user_id): return self.id


@login_manager.user_loader
def load_user(user_id):
    return UserAccount.query.get(user_id)
