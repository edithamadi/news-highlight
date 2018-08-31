from flask import Flask #import flask class from flask module
from .config import DevConfig

# Initializing application
app = Flask(__name__)

#setting up configuration
app.config.from_object(DevConfig)

from app import views #import views file from app folder
