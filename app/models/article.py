class Article:
    '''
    Article class to define News Articles Objects
    '''
    def __init__(self,name,author,description,url,urlToImage,publishedAt):
        self.name=name
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt