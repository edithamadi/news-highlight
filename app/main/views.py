from flask import render_template,redirect,url_for#import render template function from flask
from . import main#import app instance from app folder
from ..request import get_newarticle,get_sources, get_topheadlines, get_everything, search_source

# Views
@main.route('/')
def index():

    #Getting news sources
    general_newarticle = get_newarticle('general')
    technology_newarticle = get_newarticle('technology')
    entertainment_newarticle = get_newarticle('entertainment')
    sports_newarticle = get_newarticle('sports')
    business_newarticle = get_newarticle('business')
    science_newarticle = get_newarticle('science')

    title = 'Home | New Highlights'

search_source = request.args.get('article_query')

if search_source:
    return redirect(url_for('.search',source_name=search_source))
else:

    return render_template('index.html', title=title, general = general_newsource, technology = technology_newsource, entertainment = entertainment_newsource, sports = sports_newsource, business= business_newsource, science = science_newsource)


@main.route('/article/<int:article_id>')#dynamic route
def source(article_id):
    
        return render_template('article.html',id = article_id)   

#Getting articles

    article_source = get_sources(source_id,per_page)
    title = f'{source_id} | All Articles'
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',source_name=search_article))
    else:
        return render_template('article.html', title=title, name = source_id, article = article_source)

@main.route('/topheadline&<int:per_page>')
def topheadlines(per_page):
    '''
    Function that returns top headline articles
    '''

    topheadline_news = get_topheadline(per_page)

    title = 'Top Headlines'

    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('topheadline.html', title=title, name = 'Top Headlines', articles = topheadline_news)

@main.route('/everything&<int:per_page>')
def all_news(per_page):
    '''
    Function used to return all news articles
    '''

    everything_news = get_everything(per_page)

    title = 'All News'
    search_source = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('everything.html', title=title, name = 'All News', article = everything_news)

@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(articlee_name_format)
    title = f'search results for {article_name}'

    return render_template('search.html', article = searched_articles)
