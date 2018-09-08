import unittest
from models import article,source
Article = article.Article
Source = source.Source

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('abc-news','ABC News','Your trusted source for breaking news.','http://abcnews.go.com/','general','us')
        
    def test_instance(self):
        '''
        test case to test if object instance is created
        '''
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        Test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_article.id,'abc-news')
        self.assertEqual(self.new_article.name,'ABC News')
        self.assertEqual(self.new_article.description,'Your trusted source for breaking news.')
        self.assertEqual(self.new_article.url,'http://abcnews.go.com/')
        self.assertEqual(self.new_article.category,'general')
        self.assertEqual(self.new_article.country,'us')


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Article("BBC News","Theranos founder hit with criminal charges","Elizabeth Holmes is charged with fraud over claims made for blood tests her company developed.", "http://www.bbc.co.uk/news/business-44501631","https://ichef.bbci.co.uk/news/1024/branded_news/8AC7/production/_102072553_holmes.jpg","2018-06-15T22:25:40Z")

    def test_instance(self):
        '''
        test case to test if object instance is created
        '''
        self.assertTrue(isinstance(self.new_source,Source))

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        '''
        Test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_source.author,"BBC News")
        self.assertEqual(self.new_source.title,"Theranos founder hit with criminal charges")
        self.assertEqual(self.new_source.description,"Elizabeth Holmes is charged with fraud over claims made for blood tests her company developed.")
        self.assertEqual(self.new_source.url,"http://www.bbc.co.uk/news/business-44501631")
        self.assertEqual(self.new_source.urlToImage,"https://ichef.bbci.co.uk/news/1024/branded_news/8AC7/production/_102072553_holmes.jpg")
        self.assertEqual(self.new_source.publishedAt,"2018-06-15T22:25:40Z")


if __name__ == '__main__':
    unittest.main()