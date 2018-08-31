from flask import Flask #import flask class from flask module

# Initializing application
app = Flask(__name__)

from app import views #import views file from app folder
