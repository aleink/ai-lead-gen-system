def parse_thread(self, response):
    """
    Parse an individual discussion thread to see if it mentions Naples, Airbnb, or short-term
    either in the title or anywhere in the body text.
    """
    title = response.xpath("//h1/text() | //h2/text()").get()
    if not title:
        title = response.xpath("//title/text()").get() or "No Title Found"

    # Collect full thread text
    full_text_list = response.xpath("//body//text()").getall()
    full_text = " ".join(full_text_list).lower()

    # We'll unify everything in lowercase for simpler matching
    keywords = ["naples", "airbnb", "short-term", "short term"]

    # Check if any keyword appears in the combined text
    if any(kw in full_text for kw in keywords):
        yield {
            "title": title.strip(),
            "link": response.url,
        }
