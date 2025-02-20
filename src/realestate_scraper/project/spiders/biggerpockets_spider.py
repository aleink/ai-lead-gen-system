import scrapy
import re

class BiggerPocketsSpider(scrapy.Spider):
    name = "biggerpockets_spider"
    allowed_domains = ["biggerpockets.com"]
    start_urls = [
        # We'll start from the main forums page
        "https://www.biggerpockets.com/forums"
    ]

    def parse(self, response):
        """
        Parse the main forums page to find links to individual forum sections.
        Each link might look like /forums/NNN or /forums/NNN?page=X.
        We'll follow those links to gather threads.
        """
        # Example XPaths: each forum link might be an <a> with an href containing /forums/
        forum_links = response.xpath("//a[contains(@href, '/forums/')]/@href").getall()

        for link in forum_links:
            yield scrapy.Request(
                url=response.urljoin(link),
                callback=self.parse_forum
            )

    def parse_forum(self, response):
        """
        Parse an individual forum listing page, extracting thread links.
        Also handle pagination for multiple pages of threads.
        """
        # Each thread might have a URL like /forums/NNN/topics/123456
        thread_links = response.xpath(
            "//a[contains(@href, '/forums/') and contains(@href, '/topics/')]/@href"
        ).getall()

        for link in thread_links:
            yield scrapy.Request(
                url=response.urljoin(link),
                callback=self.parse_thread
            )

        # Check for pagination links (e.g., "next page")
        next_page = response.xpath("//a[contains(@rel, 'next')]/@href").get()
        if next_page:
            yield scrapy.Request(
                url=response.urljoin(next_page),
                callback=self.parse_forum
            )

    def parse_thread(self, response):
        """
        Parse an individual discussion thread to see if it mentions "Naples," "Airbnb," 
        or "short-term" in the title or anywhere in the body text.
        """
        # Attempt to grab the thread title
        title = response.xpath("//h1/text() | //h2/text()").get()
        if not title:
            title = response.xpath("//title/text()").get() or "No Title Found"

        # Collect full thread text
        full_text_list = response.xpath("//body//text()").getall()
        full_text = " ".join(full_text_list).lower()

        # We'll unify everything in lowercase for simpler matching
        keywords = ["naples", "airbnb", "short-term", "short term", "investment property"]

        # Check if any keyword appears in the combined text
        if any(kw in full_text for kw in keywords):
            yield {
                "title": title.strip(),
                "link": response.url,
            }
