from flask import render_template#import render template function from flask
from app import app#import app instance from app folder

# Views
@app.route('/')
def index():

    title = 'Welcome to The Home of the best news stories'
    return render_template('index.html', title = title)

@app.route('/article/<int:article_id>')#dynamic route
def article(article_id):
    
        return render_template('article.html',id = article_id)   

