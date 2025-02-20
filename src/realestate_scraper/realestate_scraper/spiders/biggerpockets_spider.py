import scrapy


class BiggerpocketsSpiderSpider(scrapy.Spider):
    name = "biggerpockets_spider"
    allowed_domains = ["biggerpockets.com"]
    start_urls = ["https://biggerpockets.com"]

    def parse(self, response):
        pass
