"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from __init__ import app
from models.python import python_hello
import random, json, os, requests
import subprocess

backgrounds = ["https://cdn.discordapp.com/attachments/784178874303905792/784179064378359858/Gluten-free-sushi-rolls-header.png", "https://cdn.discordapp.com/attachments/784178874303905792/784179363100098560/wp6901896.png", "https://cdn.discordapp.com/attachments/784178874303905792/784179072531824650/onmyouji-anime-girls-anime-fan-art-brunette-hd-wallpaper-preview.png", "https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

pathForImages='./images/'

f = open('data.json')
data = json.load(f)

@app.route('/')
def index():
    #response = requests.get('https://nekos.life/api/v2/img/wallpaper')
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

app.config["IMAGE_UPLOADS"]="/images"

@app.route("/upload", methods=["GET", "POST"])
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
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("homesite/login.html")
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
