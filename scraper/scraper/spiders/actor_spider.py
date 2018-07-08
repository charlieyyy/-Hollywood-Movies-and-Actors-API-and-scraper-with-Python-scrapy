import scrapy
import logging
from scraper.items import ScraperItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class ActorSpider(scrapy.Spider):
    name = "actor"

    start_urls = [
        'https://en.wikipedia.org/wiki/Brubaker'
    ]


    def parse(self, response):

        for sel in response.xpath('//h2/span[contains(text(),"Cast")]/following::ul[1]/li'):
            actorUrl = sel.xpath('a/@href').extract()[0]
            if actorUrl is not None:
                logging.info("actor url is valid")
                yield response.follow(actorUrl, callback=self.parse_actor)

    def parse_actor(self, response):

        logging.info("start scrap data from actor sites")
        info = response.xpath('//table[@class="infobox biography vcard"]')
        actorItem = ScraperItem()
        actorItem['actorName'] = info.xpath('//tr/th/span/text()')[0].extract()
        actorItem['actorAge'] = info.xpath('//tr/th[contains(text(),"Born")]/following::td[1]/text()').extract()

        yield actorItem