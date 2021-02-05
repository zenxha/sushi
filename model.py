
from flask_login import UserMixin

from db import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    filename = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

<<<<<<< HEAD
class Authentication(db.Model):
    username = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Text, nullable=False)
=======
class User(UserMixin,db.Model):
    id = db.Column(db.Text, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=True)
    password = db.Column(db.Text, nullable=False)

>>>>>>> 4cab7fbb36b6f12c21524fc28eac677cb53ce7a2
