from flask import render_template#import render template function from flask
from app import app#import app instance from app folder
from .request import get_newarticle
# Views
@app.route('/')
def index():

    #Getting news articles
    general_newarticle = get_newarticle('general')
    technology_newarticle = get_newarticle('technology')
    entertainment_newarticle = get_newarticle('entertainment')
    sports_newarticle = get_newarticle('sports')
    business_newarticle = get_newarticle('business')
    science_newarticle = get_newarticle('science')

    title = 'Home | New Highlights'
    return render_template('index.html', title=title, general = general_newarticle, technology = technology_newarticle, entertainment = entertainment_newarticle, sports = sports_newarticle, business= business_newarticle, science = science_newarticle)


@app.route('/article/<int:article_id>')#dynamic route
def article(article_id):
    
        return render_template('article.html',id = article_id)   

