from flask import render_template,redirect,url_for,#import render template function from flask
from app import app#import app instance from app folder
from .request import get_newarticle,get_sources, get_topheadlines, get_everything, search_source

# Views
@app.route('/')
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


@app.route('/article/<int:article_id>')#dynamic route
def article(article_id):
    
        return render_template('article.html',id = article_id)   


#Getting articles
    article_source = get_source(source_id,per_page)

    title = f'{source_id} | All Articles'
    search_source = request.args.get('article_query')
    if search_source:
        return redirect(url_for('.search',article_name=search_source))
    else:
        return render_template('article.html', title=title, name = source_id, articles = article_source)

@app.route('/topheadlines&<int:per_page>')
def topheadlines(per_page):
    '''
    Function that returns top headline articles
    '''

    topheadlines_news = get_topheadlines(per_page)

    title = 'Top Headlines'

    search_source = request.args.get('article_query')
    if search_source:
        return redirect(url_for('.search',article_name=search_source))
    else:
        return render_template('topheadlines.html', title=title, name = 'Top Headlines', articles = topheadlines_news)

@app.route('/everything&<int:per_page>')
def all_news(per_page):
    '''
    Function used to retirn all news articles
    '''

    everything_news = get_everything(per_page)

    title = 'All News'
    search_source = request.args.get('article_query')
    if search_source:
        return redirect(url_for('.search',article_name=search_source))
    else:
        return render_template('everything.html', title=title, name = 'All News', articles = everything_news)

@app.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'

    return render_template('search.html', articles = searched_sources)
