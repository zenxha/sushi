
from flask_login import UserMixin

from db import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
    img = db.Column(db.Text, unique=False, nullable=True)
    filename = db.Column(db.Text, nullable=False)
    satisfaction = db.Column(db.Text)
    mimetype = db.Column(db.Text, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text, nullable=False)


