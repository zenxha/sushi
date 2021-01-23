"""Views in MVC has responsibility for establishing routes and redering HTML"""
import json
import random
import requests
import sqlite3
from flask import render_template, request, redirect, url_for, session, flash, Flask, Response
from werkzeug.utils import secure_filename
from db import db_init, db
from model import Review
app = Flask(__name__)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)



backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

pathForImages='./images/'
"""
DATABASE = 'templates/homesite/Users.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        """
@app.route('/')
def index():
    #response = requests.get('https://nekos.life/api/v2/img/wallpaper')
    # background = response.json()['url']
    response = requests.get('https://api.quotable.io/random')
    quote = response.json()['content']
    author = response.json()['author']
    background = random.choice(backgrounds)
    return render_template("homesite/home.html", background=background, quote=quote, author = author)


"""our own project dstufsuf as"""

@app.route('/project')
def project():
    return render_template("homesite/project.html", background=random.choice(backgrounds))

@app.route('/base')
def base():
  return render_template("homesite/base2.html")

@app.route('/slideshow')
def slideshow():
    return render_template("homesite/slideshow.html")

"Login Section"

@app.route('/login', methods=["POST", "GET"])
def login():
    background = random.choice(backgrounds)
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("homesite/login.html", background=background)
@app.route('/upload', methods=["POST", 'GET'])
def upload():
    background = random.choice(backgrounds)
    if request.method == "POST":
        name = request.form["user_name"]
        username = request.form["user_name"]
        satisfaction = request.form["satisfaction"]
        content = request.form["content"]
        image = request.files.get('img')
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

@app.route('/signup')
@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        return render_template("homesite/user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    if "user" in session:
        user = session["user"]
        flash("You have been logged out!","warning")
    session.pop("user", None)
    return redirect(url_for("login"))
