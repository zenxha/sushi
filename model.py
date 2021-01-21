
from db import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
    mimetype = db.Column(db.Text, nullable=False)