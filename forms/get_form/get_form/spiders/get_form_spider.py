import scrapy

def generate_start_urls():
    names = ['Mark', 'Jeff', 'Darius']
    quests = ['to seek the grail', 'to learn python', 'to scrape the web']
    return ['http://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color=red'.format(name, quest) for name in names for quest in quests]

class GetFormSpiderSpider(scrapy.Spider):
    name = 'get_form_spider'
    allowed_domains = ['pythonscraping.com']
    start_urls = generate_start_urls()

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
