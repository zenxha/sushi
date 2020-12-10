"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template, request, redirect, url_for
from __init__ import app
from models.python import python_hello
import random, json

backgrounds = ["https://cdn.discordapp.com/attachments/784178874303905792/784179064378359858/Gluten-free-sushi-rolls-header.png", "https://cdn.discordapp.com/attachments/784178874303905792/784179363100098560/wp6901896.png", "https://cdn.discordapp.com/attachments/784178874303905792/784179072531824650/onmyouji-anime-girls-anime-fan-art-brunette-hd-wallpaper-preview.png", "https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

f = open('data.json')
data = json.load(f)

@app.route('/')
def index():
  background = random.choice(backgrounds)
  return render_template("homesite/home.html", background=background)



"""our own project dstufsuf as"""


@app.route('/project')
def project():
    return render_template("homesite/project.html")
@app.route('/base')
def base():
  return render_template("homesite/base2.html")
@app.route("/upload", methods=["GET", "POST"])
def upload_image():
  if request.method == "POST":

      if request.files:
          image = request.files["image"]
          print(image)
          return redirect(request.url)

  return render_template("homesite/upload.html")



"""Python Section"""


@app.route('/python/hello')
def pythonhello():
    return render_template("homesite/project.html", data=python_hello())