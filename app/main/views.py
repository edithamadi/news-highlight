from flask import render_template,redirect,url_for#import render template function from flask
from . import main#import app instance from app folder
from ..request import get_sources,get_article

# Views
@main.route('/')
def index():

    news_sources = get_sources()

    title = 'Home | New Highlights'

    return render_template('index.html', title=title, sources=news_sources)


@main.route('/article/<string:id>')
def article(id):
    articles=get_article(id)

    print(articles)

    return render_template('article.html',article=articles)
