class Source:
    '''
    Article class to define News Source Objects
    '''
    def __init__(self,id,name,description,url,category,country):
        self.id =id
        self.name =name
        self.description =description
        self.url =url
        self.category =category
        self.country =country


class Article:
    '''
    Source class to define News Articles Objects
    '''
    def __init__(self,name,author,title,description,url,urlToImage,publishedAt):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt