from app import app
import urllib.request,json
from .models import article

Article = article.Article

# Getting api key
api_key = app.config['ARTICLE_API_KEY']

# Getting the article base url
base_url = app.config["ARTICLE_API_BASE_URL"]

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

        if get_newarticle_response['articles']:
            newarticle_results_list = get_newarticle_response['articles']
            newarticle_results = process_results(newarticle_results_list)

    return newarticle_results