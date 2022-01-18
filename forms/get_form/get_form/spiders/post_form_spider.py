import scrapy
from scrapy.http import FormRequest

class GetFormSpiderSpider(scrapy.Spider):
    name = 'post_form_spider'
    allowed_domains = ['pythonscraping.com']

    def start_requests(self):
        names = ['Mark', 'Jeff', 'Darius']
        quests = ['to seek the grail', 'to learn python', 'to scrape the web']
        return [FormRequest('http://pythonscraping.com/linkedin/formAction2.php',
                              formdata={'name': name, 'quest': quest, 'color': 'blue'},
                              callback=self.parse) for name in names for quest in quests]

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
