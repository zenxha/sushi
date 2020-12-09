"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template, request, redirect, url_for
from __init__ import app
from models.java import java_ap, java_hello, java_mvc, java_event, java_study, java_details, java_projects
from models.python import python_hello, python_ap, python_flask, python_cbproj, python_study, python_details, \
    python_projects


backgrounds = ["https://cdn.discordapp.com/attachments/784178874303905792/784179064378359858/Gluten-free-sushi-rolls-header.png", "https://cdn.discordapp.com/attachments/784178874303905792/784179363100098560/wp6901896.png", "https://cdn.discordapp.com/attachments/784178874303905792/784179072531824650/onmyouji-anime-girls-anime-fan-art-brunette-hd-wallpaper-preview.png"]


@app.route('/')
def index():
    
    return render_template("homesite/home.html")


@app.route('/landing/<selection>', methods=['GET', 'POST'])
def landing(selection):
    if request.method == 'POST':  # redirection to content page
        form = request.form
        page = form['page']
        return redirect(url_for(page))
    # based off of menu selection, content is selected for landing page
    select_list = data[selection]
    heading = select_list[TITLE]
    projects = select_list[PROJECTS]
    return render_template("homesite/landing.html", heading=heading, menus=menus, projects=projects)


"""our own project dstufsuf as"""


@app.route('/project')
def project():
    return render_template("homesite/project.html")
@app.route('/base')
def base():
  return render_template("homesite/base2.html")

@app.route('/java/mvc')
def javamvc():
    return render_template("homesite/project.html", menus=menus, data=java_mvc())


@app.route('/java/ap')
def javaap():
    return render_template("homesite/project.html", menus=menus, data=java_ap())


@app.route('/java/event')
def javaevent():
    return render_template("homesite/project.html", menus=menus, data=java_event())


@app.route('/java/study')
def javastudy():
    return render_template("homesite/project.html", menus=menus, data=java_study())


"""Python Section"""


@app.route('/python/hello')
def pythonhello():
    return render_template("homesite/project.html", menus=menus, data=python_hello())


@app.route('/python/flask')
def pythonflask():
    return render_template("homesite/project.html", menus=menus, data=python_flask())


@app.route('/python/cbproj')
def pythoncbproj():
    return render_template("homesite/project.html", menus=menus, data=python_cbproj())


@app.route('/python/ap')
def pythonap():
    return render_template("homesite/project.html", menus=menus, data=python_ap())


@app.route('/python/study')
def pythonstudy():
    return render_template("homesite/project.html", menus=menus, data=python_study())


"""Git Section"""


@app.route('/git/concepts')
def gitconcepts():
    return render_template("homesite/project.html", menus=menus, data=git_concepts())


@app.route('/git/replto')
def gitreplto():
    return render_template("homesite/project.html", menus=menus, data=git_replto())


"""Pi Section"""


@app.route('/pi/webserver')
def piwebserver():
    return render_template("homesite/project.html", menus=menus, data=pi_webserver())


@app.route('/pi/portforward')
def piportforward():
    return render_template("homesite/project.html", menus=menus, data=pi_portforward())


@app.route('/pi/vncsetup')
def pivncsetup():
    return render_template("homesite/project.html", menus=menus, data=pi_vncsetup())


@app.route('/pi/realvnc')
def pirealvnc():
    return render_template("homesite/project.html", menus=menus, data=pi_realvnc())


@app.route('/pi/ssh')
def pissh():
    return render_template("homesite/project.html", menus=menus, data=pi_ssh())


"""PBL Section"""


@app.route('/pbl/overview')
def pbloverview():
    return render_template("homesite/project.html", menus=menus, data=pbl_overview())


@app.route('/pbl/scrum')
def pblscrum():
    return render_template("homesite/project.html", menus=menus, data=pbl_scrum())