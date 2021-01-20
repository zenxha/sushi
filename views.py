"""Views in MVC has responsibility for establishing routes and redering HTML"""
import json
import random
import sqlite3
from flask import g
from flask import render_template, request, redirect, url_for, session, flash

from __init__ import app

backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

pathForImages = './images/'

f = open('data.json')
data = json.load(f)
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


@app.route('/')
def index():
    # response = requests.get('https://nekos.life/api/v2/img/wallpaper')
    # background = response.json()['url']
    background = random.choice(backgrounds)
    return render_template("homesite/home.html", background=background)


"""our own project dstufsuf as"""


@app.route('/project')
def project():
    return render_template("homesite/project.html")


@app.route('/base')
def base():
    return render_template("homesite/base2.html")


@app.route('/slideshow')
def slideshow():
    return render_template("homesite/slideshow.html")


app.config["IMAGE_UPLOADS"] = "/images"

'''@app.route("/upload", methods=["GET", "POST"])'''


def upload_image():
    if request.method == "POST":

        if request.files:
            image = request.files["image"]
            image.save(pathForImages + image.filename)
            print('A user uploaded a file with the name of ' + image.filename)
            return redirect(request.url)

    return render_template("homesite/upload.html")


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
        satisfactionlevel = request.form["satisfaction"]
        print(request.form.get("satisfaction"))
        print("\n")
        if request.files:
            image = request.files["image"]
            image.save(pathForImages + image.filename)

            print(name + ' uploaded a file with the name of ' + image.filename + '\n')
            return redirect(request.url)

    return render_template("homesite/loginv2.html", background=background)


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
        flash("You have been logged out!", "warning")
    session.pop("user", None)
    return redirect(url_for("login"))
