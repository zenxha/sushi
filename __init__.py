"""_init_.py is used to define app and all blueprints"""
from datetime import timedelta

from flask import Flask
app = Flask(__name__)
app.secret_key = "heyheyhey"
app.permanent_session_lifetime = timedelta(hours=24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
