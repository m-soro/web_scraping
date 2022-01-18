import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/']


    rules = [ Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'),
              callback='parse', follow=True) ]
              
    def parse(self, response):
        return {
            "title": response.xpath('//h1/text()').get(),
            "url": response.url,
            "last_edited": response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        }
