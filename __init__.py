"""_init_.py is used to define app and all blueprints"""
from flask import Flask
app = Flask(__name__)
app.secret_key = "heyheyhey"