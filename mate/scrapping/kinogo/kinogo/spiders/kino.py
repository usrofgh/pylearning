import scrapy
from scrapy.http import Response


class KinoSpider(scrapy.Spider):
    name = 'kino'
    allowed_domains = ['kinogo.biz']
    BASE_URL = "https://kinogo.biz/"

    def start_requests(self):
        yield scrapy.Request(
            url=self.BASE_URL,
            callback=self.parse_pages,
        )

    def parse_pages(self, response: Response):
        page_count = response.css(".bot-navigation a:nth-last-child(2)::text").get()
        print("mass", page_count)

    def parse(self, response):
        pass
