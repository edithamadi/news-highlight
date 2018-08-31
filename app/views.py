from flask import render_template#import render template function from flask
from app import app#import app instance from app folder

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   title = 'Welcome to The Home of the best news stories'
    return render_template('index.html', title = title)

@app.route('/article/<int:article_id>')#dynamic route
def article(article_id):

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('article.html',id = article_id)   

