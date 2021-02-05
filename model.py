
from flask_login import UserMixin

from db import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    filename = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

class User(UserMixin,db.Model):
    id = db.Column(db.Text, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

