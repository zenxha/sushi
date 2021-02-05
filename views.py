"""Views in MVC has responsibility for establishing routes and redering HTML"""
from __init__ import create_app
import json
import random
import requests
import sqlite3
from flask import g
from flask import render_template, request, redirect, url_for, session, flash, Flask, Response, Blueprint
#from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from db import db_init, db
from model import Review, User


app = Flask(__name__)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

db = SQLAlchemy()

backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

pathForImages='./images/'
"""
DATABASE = 'templates/homesite/Users.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

<<<<<<< HEAD
app.config['MYSQL_HOST'] = '76.176.54.2'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sushi'
app.config['MYSQL_DB'] = 'usersdb'

#mysql = MySQL(app)

=======
>>>>>>> 49a86ecffd9c006a400e32eccb62b5b2218ed822
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        """

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return session.query(User).filter(User.id == userid).first()
    except model.DoesNotExist :
        return None

@app.route('/')
def index():
    #response = requests.get('https://nekos.life/api/v2/img/wallpaper')
    # background = response.json()['url']
    response = requests.get('https://api.quotable.io/random?maxLength=60')
    quote = response.json()['content']
    author = response.json()['author']
    background = random.choice(backgrounds)
    return render_template("homesite/home.html", background=background, quote=quote, author = author)


"""our own project dstufsuf as"""

@app.route('/project')
def project():
    return render_template("homesite/project.html", background=random.choice(backgrounds))

@app.route('/IAM')
def IAM():
    return render_template("easteregg/IAM.html")

@app.route('/slideshow')
def slideshow():
    return render_template("homesite/slideshow.html")

@app.route('/upload', methods=["POST", 'GET'])
@login_required
def upload():
    background = random.choice(backgrounds)
    if request.method == "POST":
        name = request.form["user_name"]
        satisfaction = request.form["satisfaction"]
        content = request.form["content"]
        image = request.files.get('img')
        if name == "mort":
            return render_template('easteregg/base.html')
        if not image:
            return 'bad news ur image didnt make it to our servers :((((', 400

        filename = secure_filename(image.filename)
        mimetype = image.mimetype
        if not filename or not mimetype:
            return 'Bad upload', 400

        review = Review(username=name, content=content, img=image.read(), filename=filename, mimetype=mimetype)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("homesite/loginv2.html", background=background)

@app.route('/images/<int:id>')
def get_img(id):
    img = Review.query.filter_by(id=id).first()
    if not img:
        return 'No img with that id', 200

    return Response(img.img, mimetype=img.mimetype)

"Login Section"

@app.route('/login', methods=["POST", "GET"])
def login_post():
    name = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    if request.method == "POST":
        user = User.query.filter_by(username=name).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect('/signup')
        # if the above check passes, then we know the user has the right credentials
        user = User(username=name, id=id, password=password)
        login_user(user, remember=remember)
        return redirect(url_for('profile'))
    return render_template('homesite/login.html')

@app.route('/profile/<int:id>')
@login_required
def profile(id):
    img = 2

    return render_template("homesite/profile.html", name=current_user.name)


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(username=name).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('signup'))

            # create a new user with the form data. Hash the password so the plaintext version isn't saved.
            new_user = User(username=name, password=generate_password_hash(password, method='sha256'))

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for(login_post))
    return render_template('homesite/signup.html')

@app.route('/user')
@login_required
def user():
    if "user" in session:
        user = session["user"]
        return render_template("homesite/user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login_post"))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
