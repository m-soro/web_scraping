import scrapy
from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from scrapy.linkextractors import LinkExtractor
from fox.items import FoxItem


class FoxScraperSpider(SitemapSpider):
    name = 'fox_scraper'
    allowed_domains = ['foxnews.com']
    sitemap_urls = ['https://www.foxnews.com/sitemap.xml?type=articles&from=1416248216000']
    # https://www.foxnews.com/us/winter-storm-midwest-threatens-travel-millions

    def parse(self, response):
        fox = FoxItem()
        fox['title'] = response.xpath('//h1/text()').get()
        fox['author'] = response.xpath('//meta[@name="dc.creator"]/@content').get()
        fox['text'] = [li.strip() for li in response.xpath('//div[@class="article-body"]/p/text()').getall()]
        fox['url'] = response.url
        return fox
