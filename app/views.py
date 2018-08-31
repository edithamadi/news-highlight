from flask import render_template#import render template function from flask
from app import app#import app instance from app folder

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'News Highlight'
    return render_template('index.html',message = message)#  The first message on the left of the = sign, represents the variable in the template. While the one to the right represents the variable in our view function.

