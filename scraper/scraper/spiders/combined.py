import scrapy
import logging
from scraper.items import ScraperItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class SpiderPlus(scrapy.Spider):
    name = "plus"
    actor_count = 0
    movie_count = 0
    start_urls = [
            'https://en.wikipedia.org/wiki/Morgan_Freeman'
    ]

    def parse(self, response):

        for sel in response.xpath('//div[@class="div-col columns column-width"]/ul/li'):
            movieUrl = sel.xpath('i/a/@href').extract()[0]
            if movieUrl is not None:
                logging.info("movie url is valid")
                yield response.follow(movieUrl, callback=self.parse_movie)
            else:
                logging.warning("Check xpath arguments")

    def parse_movie(self, response):

        logging.info("start scrap data from movie sites")
        table = response.xpath('//table[@class="infobox vevent"]')
        movieItem = ScraperItem()
        movieItem['movieName'] = table.xpath('//tr/th/text()')[0].extract()
        movieItem['movieYear'] = table.xpath('//tr/th/div[contains(text(),"Release date")]/following::td/div/ul/li[1]/text()').extract_first()
        movieItem['movieGrossing'] = table.xpath('//tr/th[contains(text(),"Box office")]/following::td/text()').extract_first()
        movieItem['actorlist'] = response.xpath('//h2/span[contains(text(),"Cast")]/following::ul[1]/li/a/text()').extract()

        self.movie_count += 1
        logging.debug("movie scraped: ")
        print(self.movie_count)

        yield movieItem

        for sel in response.xpath('//h2/span[contains(text(),"Cast")]/following::ul[1]/li'):
            actorUrl = sel.xpath('a/@href').extract()[0]
            if (actorUrl is not None) and (self.actor_count <= 250):
                logging.info("actor url is valid")
                yield response.follow(actorUrl, callback=self.parse_actor)


    def parse_actor(self, response):

        logging.info("start scrap data from actor sites")
        info = response.xpath('//table[@class="infobox biography vcard"]')
        actorItem = ScraperItem()
        actorItem['actorName'] = info.xpath('//tr/th/span/text()')[0].extract()
        actorItem['actorAge'] = info.xpath('//tr/th[contains(text(),"Born")]/following::td[1]/text()').extract()
        actorItem['movielist'] = response.xpath('//h2/span[contains(text(),"Filmography")]/following::ul[1]/li/i/a/text()').extract()

        self.actor_count += 1
        logging.debug("actor scraped: ")
        print(self.actor_count)

        yield actorItem

        for sel in response.xpath('//h2/span[contains(text(),"Filmography")]/following::ul[1]/li'):
            movieUrl = sel.xpath('i/a/@href').extract()[0]
            if (movieUrl is not None) and (self.movie_count <= 125):
                logging.info("movie url is valid")
                yield response.follow(movieUrl, callback=self.parse_movie)