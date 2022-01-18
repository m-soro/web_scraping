import scrapy

class LoggingPythonScraperSpider(scrapy.Spider):
    name = 'logging_python_scraper'
    allowed_domains = ['pythonscraping.com/']
    start_urls = ['http://pythonscraping.com/linkedin/cookies/profile.php']

    def make_requests_from_url(self, url):
        request = super(LoggingPythonScraperSpider, self).make_requests_from_url(url)
        request.cookies['username'] = 'Mark!!!!'
        request.cookies['loggedin'] = '1'
        return request

    def parse(self, response):
        return { 'text': response.xpath('//body/text()').get() }
