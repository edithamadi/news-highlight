import os # import os module that will allow our application to interact 
           # with the operating systemdependent functionality

class Config:
    '''
    General configuration parent class
    '''

    SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?&apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SECRET_KEY = os.environ.get ( 'SECRET_KEY' )
    SOURCE_API_KEY =os.environ.get('SOURCE_API_KEY')
    # SOURCES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us{}&apiKey={}'

class ProdConfig(Config):

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

# create a dictionary config_options to help us access different configuration option classes.

config_options = {
'development':DevConfig,
'production':ProdConfig
}


