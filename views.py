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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

db = SQLAlchemy()

backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

pathForImages='./images/'

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

@app.route('/browse')
def browse():
    review_query = Review.query.all()
    reviews = []
    for review in review_query:
        review_dict = {
            'id': review.id,
            'username': review.username,
            'content': review.content,
            'satisfaction': review.satisfaction,
            'image':  'http://localhost:5000/images/' + str(review.id)
        }
        reviews.append(review_dict)
    return render_template("homesite/browse.html", reviews=reviews, background=random.choice(backgrounds))

@app.route('/upload', methods=["POST", 'GET'])
def upload():
    background = random.choice(backgrounds)
    if request.method == "POST":
        name = request.form["user_name"]
        satisfaction = request.form["satisfaction"]
        content = request.form["content"]
        image = request.files.get('img')
        if name == "mort":
            return render_template('easteregg/IAM.html')
        if not image:
            return 'bad news ur image didnt make it to our servers :((((', 400

        filename = secure_filename(image.filename)
        mimetype = image.mimetype
        if not filename or not mimetype:
            return 'Bad upload', 400

        review = Review(username=name, content=content, img=image.read(), filename=filename, satisfaction=satisfaction,mimetype=mimetype)
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

    return render_template('homesite/login.html')

@app.route('/profile/<int:id>')
def profile(id):
    img = 2
    return "o"


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        user = User.query.filter_by(username=username).first() # if this returns a user, then the email already exists in database

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
