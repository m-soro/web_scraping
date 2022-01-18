import scrapy
import time
from scrapy_selenium import SeleniumRequest

def wait(driver):
    time.sleep(1)
    return True

class SeleniumBotSpiderSpider(scrapy.Spider):
    name = 'selenium_bot_spider'
    allowed_domains = ['dunkindonuts.com']
    start_urls = ['https://www.dunkindonuts.com/en/locations?location=22303']


    def make_requests_from_url(self, url):
        return SeleniumRequest(url=url, wait_time=10, wait_until=wait)


    def parse(self, response):
        return { 'addresses': response.xpath(
        '//div[@class="store-item__address--line1"]/a/text()').getall() }
