import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/"]

    def parse(self, response):
        # Extract the page title
        page_title = response.xpath("//title/text()").get()
        # Yield data as a dictionary
        yield {
            "title": page_title
        }
