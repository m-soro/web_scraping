import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_collector.items import ArticleCollectorItem

class WikipediaArticleCollectorSpider(CrawlSpider):
    name = 'wikipedia_article_collector'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Kevin_Bacon']

    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse', follow=True)]

    def parse(self, response):
        article = ArticleCollectorItem()
        article['title'] = response.xpath('//h1/text()').get(),
        article['url'] = response.url,
        article['last_edited'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article
