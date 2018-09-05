import urllib.request,json
from datetime import datetime
from .models import Article
from .models import Source

Article = article.Article

# # Getting api key
# api_key = app.config['ARTICLE_API_KEY']
# # Getting the article base url
# base_url = app.config["ARTICLE_API_BASE_URL"]


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
    global api_key,base_url,source_url,topheadline_url,everything_url,search_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["ARTICLE_API_BASE_URL"]
    source_url = app.config["EVERYTHING_SOURCE_BASE_URL"]
    topheadline_url = app.config["TOP_HEADLINES_BASE_URL"]
    everything_url =app.config["EVERYTHING_BASE_URL"]
    search_url = app.config["SEARCH_API_BASE_URL"]



def get_newarticle(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newarticle_url = base_url.format(category,api_key)
    print(get_newarticle_url)

    with urllib.request.urlopen(get_newarticle_url) as url:
        get_newarticle_data = url.read()
        get_newarticle_response = json.loads(get_newarticle_data)

        newarticle_results = None

        if get_newarticle_response['sources']:
            newarticle_results_list = get_newarticle_response['sources']
            newarticle_results = process_results(newarticle_results_list)

    return newarticle_results

def process_results(newarticle_list):
    '''
    Function  that processes the new source result and transform them to a list of Objects
    Args:
        newarticle_list: A list of dictionaries that contain news source details
    Returns :
        newarticle_results: A list of newarticle objects
    '''
    newarticle_results = []
    for news_item in newarticle_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        publishedAt = news_item.get('publishedAt')

        newarticle_object = Article(id,name,description,url,category,publishedAt)
        newarticle_results.append(newarticle_object)

    return newarticle_results

def get_sources(source_id,limit):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(source_id,limit,api_key)
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['articles']:
            sources_results_list = get_sources_response['articles']
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(articles_list):
    '''
    Function  that processes the new articles and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain article details
    Returns :
        sources_results: A list of article objects
    '''
    sources_results = []
    for source_item in sources_list:
        author = source_item.get('author')
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        urlToImage = source_item.get('urlToImage')
        publishedAt = source_item.get('publishedAt')

        publishedAt = datetime(year=int(publishedAt[0:4]),month=int(publishedAt[5:7]),day=int(publishedAt[8:10]),hour=int(publishedAt[11:13]),minute=int(publishedAt[14:16]))

        if urlToImage:
            sources_object = Source(author, title, description, url, urlToImage, publishedAt)
            sources_results.append(sources_object)

    return sources_results

def get_topheadlines(limit):
    '''
    Function that gets the json response to our url request
    '''
    get_topheadlines_url = topheadline_url.format(limit,api_key)
    print(get_topheadlines_url)

    with urllib.request.urlopen(get_topheadlines_url) as url:
        get_topheadlines_data = url.read()
        get_topheadlines_response = json.loads(get_topheadlines_data)

        topheadlines_results = None

        if get_topheadlines_response ['articles']:
            topheadlines_results_list = get_topheadlines_response['articles']
            topheadlines_results = process_sources(topheadlines_results_list)

    return topheadlines_results


def get_everything(limit):
    '''
    Function that gets the json response to our url request
    '''
    get_everything_url = everything_url.format(limit,api_key)
    print(get_everything_url)

    with urllib.request.urlopen(get_everything_url) as url:
        get_everything_data = url.read()
        get_everything_response = json.loads(get_everything_data)

        everything_results = None

        if get_everything_response['articles']:
            everything_results_list = get_everything_response['articles']
            everything_results = process_sources(everything_results_list)

    return everything_results


def search_article(article_name):
    get_search_url = search_url.format(article_name,api_key)

    with urllib.request.urlopen(get_search_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_sources(search_article_list)

    return search_article_results
