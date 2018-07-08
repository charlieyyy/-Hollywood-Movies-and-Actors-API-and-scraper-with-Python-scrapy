import scrapy
import logging
from scraper.items import ScraperItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class MovieSpider(scrapy.Spider):
    name = "movie"
    count = 0

    start_urls = [
            'https://en.wikipedia.org/wiki/Morgan_Freeman',
            #'https://en.wikipedia.org/wiki/Tom_Cruise',
    ]

    def parse(self, response):

        for sel in response.xpath('//div[@class="div-col columns column-width"]/ul/li'):
            movieUrl = sel.xpath('i/a/@href').extract()[0]
            if movieUrl is not None:
                logging.info("movie url is valid")
                self.count +=1
                yield response.follow(movieUrl, callback=self.parse_movie)
                logging.debug("movie scraped: ")
                print(self.count)

    def parse_movie(self, response):

        logging.info("start scrap data from movie sites")
        table = response.xpath('//table[@class="infobox vevent"]')
        movieItem = ScraperItem()
        movieItem['movieName'] = table.xpath('//tr/th/text()')[0].extract()
        movieItem['movieYear'] = table.xpath('//tr/th/div[contains(text(),"Release date")]/following::td/div/ul/li[1]/text()').extract_first()
        movieItem['movieGrossing'] = table.xpath('//tr/th[contains(text(),"Box office")]/following::td/text()').extract_first()

        yield movieItem