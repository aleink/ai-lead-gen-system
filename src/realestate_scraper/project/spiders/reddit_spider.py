# reddit_spider.py

import scrapy
import re

class RedditSpider(scrapy.Spider):
    name = "reddit_spider"
    allowed_domains = ["reddit.com"]
    start_urls = [
        "https://www.reddit.com/r/realestateinvesting/new/"
    ]

    def parse(self, response):
        """
        Parses the listing of new posts on r/realestateinvesting.
        We look for titles containing 'Naples', 'Airbnb', or 'short-term'.
        """
        # Reddit's current layout often stores posts in <div data-testid='post-container'> or <div class='Post ...'>
        # We'll try a broad XPATH or CSS selector to find post containers.
        posts = response.xpath("//div[contains(@data-testid, 'post-container')]")

        for post in posts:
            title = post.xpath(".//h3/text()").get()
            post_link = post.xpath(".//a/@href").get()

            if title:
                # Check if title mentions any relevant keywords
                keywords = re.compile(r"(naples|airbnb|short[\s-]*term)", re.IGNORECASE)
                if keywords.search(title):
                    yield {
                        "title": title.strip(),
                        # Convert relative link to absolute URL
                        "link": response.urljoin(post_link)
                    }

        # Attempt to follow "next page" link. In many subreddits, it’s loaded dynamically, so we might not find a typical pagination link.
        # If Reddit changes the structure, you may need to adapt this logic or use the official Reddit API.
        next_page = response.xpath("//a[contains(@rel, 'nofollow next')]/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
