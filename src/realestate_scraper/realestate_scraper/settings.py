# settings.py

BOT_NAME = "realestate_scraper"

SPIDER_MODULES = ["realestate_scraper.spiders"]
NEWSPIDER_MODULE = "realestate_scraper.spiders"

# IMPORTANT: Disable robots.txt obedience for testing
ROBOTSTXT_OBEY = False

# Use a custom User-Agent so Reddit doesn’t reject default Scrapy UA
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/110.0.0.0 Safari/537.36'
}

# Configure item pipelines
ITEM_PIPELINES = {
    'realestate_scraper.pipelines.PostgresPipeline': 300,
}

# (Optional) Adjust concurrency or delays to be more polite
# DOWNLOAD_DELAY = 1
# CONCURRENT_REQUESTS_PER_DOMAIN = 8
