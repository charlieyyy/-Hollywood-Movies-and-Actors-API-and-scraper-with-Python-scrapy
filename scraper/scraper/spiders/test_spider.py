import scrapy
import logging
from scraper.items import ScraperItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ["https://en.wikipedia.org/wiki/Morgan_Freeman"]


    def parse(self, response):

        info = response.xpath('//table[@class="infobox biography vcard"]')
        actorItem = ScraperItem()
        actorItem['actorName'] = info.xpath('//tr/th/span/text()')[0].extract()
        actorItem['actorAge'] = info.xpath('//tr/th[contains(text(),"Born")]/td/text()').extract()

        print(actorItem)

        for sel in response.xpath('//div[@class="div-col columns column-width"]/ul/li'):
            movieUrl = sel.xpath('i/a/@href').extract()[0]
            if movieUrl is not None:
                logging.info("movie url is valid")
                yield response.follow(movieUrl, callback=self.parse_movie)

    def parse_movie(self, response):

        logging.info("start scrap data from movie sites")
        table = response.xpath('//table[@class="infobox vevent"]')
        movieItem = ScraperItem()
        movieItem['movieName'] = table.xpath('//tr/th/text()')[0].extract()
        movieItem['movieYear'] = table.xpath('//tr/th/div[contains(text(),"Release Date")]/text()').extract()
        movieItem['movieGrossing'] = table.xpath('//tr/th[contains(text(),"Box Office")]/td/text()').extract()
        # table.xpath('//tr/th/span/text()')[0].extract()

        yield movieItem

        for actor in response.xpath('//div[@class="div-col columns column-count column-count-2"]/ul/li'):
            actorUrl = actor.xpath('a/@href').extract()[0]
            if actorUrl is not None:
                logging.info("actor url is valid")
                yield response.follow(movieUrl, callback=self.parse)