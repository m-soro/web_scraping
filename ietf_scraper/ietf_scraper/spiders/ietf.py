import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscrping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        return {
                "Title": response.xpath('//span[@class="title"]/text()').get(),
                "Subheadings": response.xpath('//span[@class="subheading"]/text()').getall(),
                "Date using Meta": response.xpath('//meta[@name="DC.Date.Issued"]/@content').get(),
                "Author using Meta": response.xpath('//meta[@name="DC.Creator"]/@content').get(),
                "Author using html tags": response.xpath('//span[@class="author-name"]/text()').get(),
                "Text": response.xpath('//div[@class="text"]').get(),
                "Author's Address": response.xpath('//span[@class="address"]/text()').get()
        }
