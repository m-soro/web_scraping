import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from fox.items import FoxItem


class FoxScraperSpider(CrawlSpider):
    name = 'fox_scraper'
    allowed_domains = ['foxnews.com']
    start_urls = ['http://foxnews.com/us']
    # https://www.foxnews.com/us/winter-storm-midwest-threatens-travel-millions
    # rules = [Rule(LinkExtractor(allow=r'^(?!.*.print).*'), callback='parse', follow=True)]
    rules = [Rule(LinkExtractor(allow='us/'), callback='parse', follow=True)]

    def parse(self, response):
        fox = FoxItem()
        fox['title'] = response.xpath('//h1/text()').get()
        fox['author'] = response.xpath('//meta[@name="dc.creator"]/@content').get()
        fox['text'] = [li.strip() for li in response.xpath('//div[@class="article-body"]/p/text()').getall()]
        fox['url'] = response.url
        return fox
