"""_init_.py is used to define app and all blueprints"""
from datetime import timedelta
from flask import Flask

from flask_login import LoginManager
from db import db

def create_app():
    app = Flask(__name__)

    app.secret_key = 'heyheyhey'
    app.permanent_session_lifetime = timedelta(hours=24)
    app.config['SECRET_KEY'] = 'heyheyhey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from model import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))