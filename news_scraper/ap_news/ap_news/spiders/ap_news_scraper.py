import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ap_news.items import ApNewsItem
from datetime import datetime
import json

class ApNewsScaperSpider(CrawlSpider):
    name = 'ap_news_scaper'
    allowed_domains = ['apnews.com']
    start_urls = ['http://apnews.com/']
    rules = [Rule(LinkExtractor(allow='article/'), callback='parse', follow=True)]

    def parse(self, response):
        jsonData = json.loads(response.xpath('//script[@data-rh="true"]/text()').get())
        ap_news = ApNewsItem()
        ap_news['title'] = response.xpath('//h1/text()').get()
        ap_news['date'] =  datetime.strptime(jsonData['datePublished'][:10], '%Y-%m-%d').date()
        ap_news['author'] = jsonData['author'][0]
        ap_news['description'] = jsonData['description']
        ap_news['text'] = [li.strip() for li in response.xpath('//div[@class="Article"]/p/text()').getall()]
        ap_news['url'] = response.url
        return ap_news
