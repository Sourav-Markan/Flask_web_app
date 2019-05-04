from flask import *
from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_user import login_required, SQLAlchemyAdapter, UserManager, UserMixin
from flask_user import roles_required
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

class User(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    username = db.Column(db.String(20))
    first_name = db.Column(db.String(20))
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    password = db.Column(db.String(255))
    user_type = db.Column(db.String(20))

    def __init__(self, first_name, middle_name, last_name, email, username,user_type, password):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.user_type = user_type

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "User { Name: %r }" % (self.username)

db.create_all()