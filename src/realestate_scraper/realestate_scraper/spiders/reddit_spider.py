import scrapy
import re

class RedditSpider(scrapy.Spider):
    name = "reddit_spider"
    allowed_domains = ["reddit.com"]
    start_urls = [
        "https://www.reddit.com/r/realestateinvesting/new/"  # We'll scrape the 'new' posts for demonstration
    ]

    def parse(self, response):
        # Each post is in a <div> or <article> that contains the post title and link
        posts = response.xpath("//div[contains(@data-testid, 'post-container')]")
        for post in posts:
            title = post.xpath(".//h3/text()").get()
            post_link = post.xpath(".//a/@href").get()

            # If there's no title, skip
            if not title:
                continue

            # Check if title mentions 'Naples', 'Airbnb', or 'short-term'
            # (You can add more keywords or refine the regex as needed)
            keywords = re.compile(r"(naples|airbnb|short[\s-]*term)", re.IGNORECASE)
            if keywords.search(title):
                yield {
                    "title": title.strip(),
                    "link": response.urljoin(post_link),
                }

        # Pagination: Attempt to follow "next" link if available
        next_page = response.xpath("//a[contains(text(), 'Next')]/@href").get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
