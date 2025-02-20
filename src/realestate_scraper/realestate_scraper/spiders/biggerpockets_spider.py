# biggerpockets_spider.py

import scrapy
import re

class BiggerPocketsSpider(scrapy.Spider):
    name = "biggerpockets_spider"
    allowed_domains = ["biggerpockets.com"]
    start_urls = [
        # We can start by scraping the main forums page
        "https://www.biggerpockets.com/forums"
    ]

    def parse(self, response):
        """
        Parse the main forums page to find forum topic links or categories.
        Then follow those links to scrape actual discussion threads.
        """
        # Example: Each forum category might be in an <a> link
        forum_links = response.xpath("//a[contains(@href, '/forums/')]/@href").getall()
        # Convert them to absolute URLs
        for link in forum_links:
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_forum)

    def parse_forum(self, response):
        """
        Parse an individual forum or topic listing, looking for threads.
        """
        # Example: Each thread might appear in <div> or <li> with a link to the thread
        thread_links = response.xpath("//a[contains(@href, '/forums/') and contains(@href, '/topics/')]/@href").getall()

        for link in thread_links:
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_thread)

        # Look for pagination links to additional pages of threads
        next_page = response.xpath("//a[contains(@rel, 'next')]/@href").get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse_forum)

    def parse_thread(self, response):
        """
        Parse an individual discussion thread to see if it mentions Naples, Airbnb, or short-term.
        """
        # Thread title might be in an <h1> or <h2> tag
        title = response.xpath("//h1/text() | //h2/text()").get()
        if not title:
            title = response.xpath("//title/text()").get()  # fallback

        if title:
            # Check if title or the page content mentions relevant keywords
            # We'll do a basic check on the title for now
            keywords = re.compile(r"(naples|airbnb|short[\s-]*term)", re.IGNORECASE)
            if keywords.search(title):
                yield {
                    "title": title.strip(),
                    "link": response.url,
                }

        # (Optional) If you want to check the entire thread content, do:
        # full_text = " ".join(response.xpath("//body//text()").getall())
        # if keywords.search(full_text):
        #     yield { "title": title.strip(), "link": response.url }

