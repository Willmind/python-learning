import scrapy


class Db250Spider(scrapy.Spider):
    name = 'db250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        pass
