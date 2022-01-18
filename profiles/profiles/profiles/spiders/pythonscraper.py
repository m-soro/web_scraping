import scrapy
import time
from scrapy_selenium import SeleniumRequest

def wait(driver):
    time.sleep(1)
    return True

class PythonscraperSpider(scrapy.Spider):
    name = 'pythonscraper'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/cookies/login.html']

    def make_requests_from_url(self, url):
        return SeleniumRequest(url=url, wait_time=10, wait_until=wait)

    def parse(self, response):
        driver = response.request.meta['driver']

        username = driver.find_element_by_xpath('//input[@name="username"]')
        username.send_keys('Mark!!!')

        password = driver.find_element_by_xpath('//input[@name="password"]')
        password.send_keys('password')

        submit = driver.find_element_by_xpath('//input[@type="submit"]')
        submit.click()

        time.sleep(5)

        profile_link = driver.find_element_by_xpath('//a[@href="profile.php"]')
        profile_link.click()

        time.sleep(5)

        return { 'text': response.xpath('//body/text()').get() }
