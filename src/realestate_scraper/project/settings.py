# settings.py

BOT_NAME = "project"

SPIDER_MODULES = ["project.spiders"]
NEWSPIDER_MODULE = "project.spiders"

# ---------------------------------------------------------------------------
# Robotstxt and User-Agent
# ---------------------------------------------------------------------------
# For testing purposes, we'll ignore robots.txt. 
# (In production, you should carefully consider site TOS and robots.txt.)
ROBOTSTXT_OBEY = False

# A custom User-Agent to reduce likelihood of being blocked:
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/110.0.0.0 Safari/537.36"
    )
}

# ---------------------------------------------------------------------------
# Throttling & Concurrency
# ---------------------------------------------------------------------------
# Enable AutoThrottle to adaptively control crawl speed based on server load.
AUTOTHROTTLE_ENABLED = True
# Initial download delay
AUTOTHROTTLE_START_DELAY = 3.0
# Maximum download delay in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30.0
# Target concurrency
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for each response
AUTOTHROTTLE_DEBUG = False

# Also set a manual download delay to avoid hitting the site too hard.
DOWNLOAD_DELAY = 3  # seconds between requests to the same domain

# Limit the total number of concurrent requests
CONCURRENT_REQUESTS = 2
CONCURRENT_REQUESTS_PER_DOMAIN = 2

# ---------------------------------------------------------------------------
# Item Pipelines
# ---------------------------------------------------------------------------
# We use the PostgresPipeline to store scraped data in PostgreSQL
ITEM_PIPELINES = {
    "project.pipelines.PostgresPipeline": 300,
}


# ---------------------------------------------------------------------------
# Other Default Scrapy Settings (Optional to keep or remove)
# ---------------------------------------------------------------------------
# USER_AGENT = 'realestate_scraper (+http://www.yourdomain.com)'
# COOKIES_ENABLED = False
# TELNETCONSOLE_ENABLED = False
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }
# SPIDER_MIDDLEWARES = {
#    'realestate_scraper.middlewares.RealestateScraperSpiderMiddleware': 543,
# }
# DOWNLOADER_MIDDLEWARES = {
#    'realestate_scraper.middlewares.RealestateScraperDownloaderMiddleware': 543,
# }
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
