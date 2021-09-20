"""Views in MVC has responsibility for establishing routes and rendering HTML"""

from __init__ import app
import random
import requests
import flask, json
from flask import g, jsonify
from flask import render_template, request, redirect, url_for, session, flash, Flask, Response, Blueprint

from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import pingip
#from db import db_init, db
from model import Review, User
from flask_user import roles_required
with open('config.json') as file:
    config = json.load(file)


app = Flask(__name__)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db_init(app)

db = SQLAlchemy()

backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

pingip

pathForImages='./images/'
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/')
def index():
    response = requests.get('https://nekos.life/api/v2/img/wallpaper')
    background = response.json()['url']
    response = requests.get('https://api.quotable.io/random?maxLength=60')
    quote = response.json()['content']
    author = response.json()['author']
    background = random.choice(backgrounds)
    return render_template("homesite/home.html", background=background, quote=quote, author = author)

"""our own project dstufsuf as"""

@app.route('/ping', methods=["POST", 'GET'])
@roles_required('Admin')
def upload():
    return render_template("homesite/loginv2.html")


@app.route('/login', methods=["POST", "GET"])
def login_post():
    if request.method == "POST":
        password = request.form.get('password')
        name = request.form.get("username")
        users = User.query.filter_by(username=name)
        for user in users:
            if not user: return render_template('homesite/signup.html', error="Please sign up for an account first")
            if user.password == password:
                session.pop('user', None)
                session['user'] = user.username
                return redirect(url_for('upload'))
        if name == "mort":
            return render_template('easteregg/IAM.html')
        return render_template('homesite/login.html', error="Please check your credentials and try again", background = random.choice(backgrounds))

    return render_template("homesite/login.html", background = random.choice(backgrounds))


"""
@app.route('/profile/<int:id>')
def profile(id):
    img = 2

    return render_template("homesite/profile.html", name=current_user.name)
"""


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if name == "mort": # easter egg
            return render_template('easteregg/IAM.html')

        user = User.query.filter_by(username=name).first() # if this returns a user, then the email already exists in database

        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            return "choose a new username"
        else:
            # create a new user with the form data. Hash the password so the plaintext version isn't saved.
            new_user = User(username=name, password=password, email=email)

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("login_post"))
    return render_template('homesite/signup.html', background = random.choice(backgrounds))


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for("index"))
