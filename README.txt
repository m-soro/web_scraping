# Web Scraping

Target website: http://pythonscraping.com/linkedin/ietf.html

//h1 -- select any h1 on the page
//div/h1 -- select any h1 tag that are immediate child of div tag
//div//h1 -- select any h1 tag that falls anywhere under div tag, regardless of whether or not its an immediate child of div

//span[@class="title"]/text()
//span[@class="title"]/@id

Using meta tag:
"Author using Meta": response.xpath('//meta[@name="DC.Creator"]/@content').get()

using HTML tags:
"Title": response.xpath('//span[@class="title"]/text()').get()
"title": response.xpath('//title/text()').get()


Building a crawler

we use:

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

and

class WikipediaSpider(CrawlSpider):

and inside the class is a rule:

rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse', follow=True)]

Importing items module

from fox.items import FoxItem

then under the parse function:

fox = FoxItem()


Using Json

import json

inside parse function

jsonData = json.loads(response.xpath('//article[@role="article"]/script[@type="application/ld+json"]/text()').get())
or jsonData = json.loads(response.xpath('//script[@data-rh="true"]/text()').get())

article['title'] = jsonData['headline']
article['description'] = jsonData['description']
article['title'] = jsonData['headline']
article['author'] = jsonData['author']['name']


Quick shortcut to run the wikipedia_article_collector.py
scrapy runspider wikipedia_article_collector.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10

building a selenium scrapy spider

Add this to settings.py

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = '/Users/marksoro/chromedriver'
SELENIUM_DRIVER_ARGUMENTS =[]

also add middlewares

DOWNLOADER_MIDDLEWARES = {
   'selenium_spider.middlewares.SeleniumSpiderDownloaderMiddleware': 543,
   'scrapy_selenium.SeleniumMiddleware':800
}
