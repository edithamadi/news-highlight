import urllib.request,json
from datetime import datetime
from .models import Source,Article


# Getting api key
api_key = None
#Getting the movie base url
base_url = None
#Getting the source base url
source_url = None
#Getting the topheadline articles
topheadline_url = None
#Getting all articles
everything_url = None
#Search url
search_url = None


def configure_request(app):
    global api_key,source_url,article_url
    api_key = app.config['SOURCE_API_KEY']
    source_url = app.config["SOURCES_API_BASE_URL"]
    article_url = app.config["ARTICLE_API_BASE_URL"]
    

article_base_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_news_details_url = source_url.format(api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources_list = get_news_response['sources']
            news_sources = process_sources(news_sources_list)

    return news_sources

def process_sources(sources_list):
    '''
    Function  that processes the new source result and transform them to a list of Objects
    Args:
        newarticle_list: A list of dictionaries that contain news source details
    Returns :
        newarticle_results: A list of newarticle objects
    '''
    news_sources = []
    for news_item in sources_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')
        news_source_object = Source(id,name,description,url,category,country)
        news_sources.append(news_source_object)

    return news_sources

def get_article(id):
    get_article_details_url= article_base_url.format(id,api_key)
    with urllib.request.urlopen(get_article_details_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        news_articles = None

        if get_article_response['articles']:
            news_articles_list = get_article_response['articles']
            news_articles = process_articles(news_articles_list)
    return news_articles

def process_articles(articles_list):
    news_articles = []
    for article_item in articles_list:
        name = article_item.get ( 'name' )
        author = article_item.get ('author')
        title = article_item.get ( 'title' )
        description = article_item.get ('description')
        url = article_item.get ('url')
        urlToImage = article_item.get ( 'urlToImage' )
        publishedAt = article_item.get ('publishedAt' )
        articles_object=Article(name, author,title,description,url,urlToImage,publishedAt)
        news_articles.append(articles_object)

    return news_articles
