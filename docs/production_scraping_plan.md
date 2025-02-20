# Production Scraping Plan

## 1. Target Websites/Platforms

Below are the real data sources we intend to scrape or query for leads—specifically, individuals or entities interested in purchasing Airbnb investment properties in Naples:

1. **Real Estate Forums & Communities**  
   - **BiggerPockets**: A popular forum where real estate investors discuss deals, financing, and strategies.  
     - **Access Method**: HTML scraping (no official public API). Must check forum rules and Terms of Service.  
     - **Data Points**: Usernames, discussion posts mentioning “Naples” or “Airbnb,” user profile details (if publicly visible), contact info if shared.  
     - **Restrictions**: Must respect robots.txt and TOS. Potential need for rotating proxies or a “light touch” scraping approach to avoid bans.

   - **Reddit** (e.g., r/realestateinvesting, r/AirBnB):  
     - **Access Method**: Official Reddit API (limited free tier) or HTML scraping.  
     - **Data Points**: Post titles, post bodies mentioning “Naples” or “short-term rental,” user flair (if relevant), public user data.  
     - **Restrictions**: The Reddit API has rate limits; HTML scraping also has TOS implications.

   - **Facebook Groups** (Real Estate Investing Groups, Naples Local Groups):  
     - **Access Method**: No official public API for group data. Typically must scrape via a logged-in session or use third-party tools.  
     - **Data Points**: Group posts mentioning “Naples investment,” user names, any contact details shared in posts.  
     - **Restrictions**: Facebook is strict about scraping. May need rotating IPs or manual data extraction. Potential risk of account ban if not done carefully.

2. **Real Estate Listing Platforms**

   - **Zillow** / **Realtor.com**:  
     - **Access Method**: Zillow’s unoffical or limited free APIs, or HTML scraping.  
     - **Data Points**: Listing addresses, price, listing agent info, property details. Potential to cross-reference owners/investors.  
     - **Restrictions**: TOS often prohibits unauthorized scraping. Must be mindful of usage limits and disclaimers.

   - **MLS (Multiple Listing Service) Data** (where publicly accessible or with permission):
     - **Access Method**: Some MLS providers offer official APIs or data export for licensed realtors.  
     - **Data Points**: Owner information, property details, days on market, etc.  
     - **Restrictions**: Often requires a realtor license or special permission.

3. **Public Records (Naples / Collier County)**  
   - **County Tax Assessor/Property Appraiser Sites**:  
     - **Access Method**: Usually HTML scraping. Some counties offer open data portals.  
     - **Data Points**: Owner name, mailing address, property classification, sale history.  
     - **Restrictions**: Typically public info, but watch for usage disclaimers or request limits.

---

## 2. Data Points to Extract

We aim to gather enough information to identify, validate, and engage potential investors. Key fields include:

- **Name / Username** (for personal or entity identification)
- **Email Address** (if publicly provided or derivable)
- **Phone Number** (if shared or part of a listing)
- **Property Details** (address, price range, rental history, if relevant)
- **Location Mention** (must mention “Naples” or “Southwest Florida”)
- **Investment Interest** (keywords like “Airbnb,” “short-term rental,” “vacation rental,” etc.)
- **Social Media / Forum Profile Links** (for outreach or verification)
- **Engagement Indicators** (frequency of posts, responses to “Naples Airbnb” topics, etc.)

**Filtering Criteria**:  
- Must explicitly mention “Naples” or show property location in Collier County.
- Must have expressed interest in Airbnb, short-term rentals, or real estate investing.
- Email or direct contact method must be discoverable or provided.  
- Optional: Sufficient evidence of real estate experience (e.g., multiple posts, references to existing properties).

---

## 3. Database/Storage Approach

For a **production-grade** setup, we plan to move beyond SQLite:

- **Primary Choice**: **PostgreSQL**  
  - **Why**: Reliable, open-source, good support for complex queries and indexing.  
  - **Deployment**: Could host on AWS RDS (still within a free tier for small usage) or on a self-managed server.  
  - **Structure**:  
    - **investors** table (id, name, email, phone, source, date_found, etc.)  
    - **properties** table (id, address, city, county, property_details, owner_id, etc.)  
    - Additional relational tables for cross-referencing forum user profiles or lead scoring.

- **Potential Alternative**: **MySQL** or **MariaDB** if that fits existing hosting environments.

- **Cloud Integration**:  
  - If we need higher scalability or advanced features, we can host PostgreSQL on AWS, Google Cloud SQL, or Azure.  
  - We’ll ensure SSL connections and proper credentials to protect investor data.

---

## 4. Additional Tools & Considerations

- **Rotating Proxies / VPN**:  
  - Services like ScraperAPI, ProxyCrawl, or custom proxy pools to avoid IP bans and handle sites with anti-scraping measures.

- **Headless Browsers (Selenium / Playwright)**:  
  - Necessary if certain pages require JavaScript to render (e.g., dynamic content, infinite scrolling).  
  - Will add overhead but often crucial for modern web apps.

- **AI-Based Text Analysis**:  
  - Use NLP libraries (e.g., spaCy, Transformers) to identify leads mentioning “Naples,” “Airbnb,” or “short-term rental.”  
  - Could later incorporate sentiment analysis or advanced classifiers to score leads more effectively.

- **Authentication / Cookies Handling**:  
  - Some sites (e.g., Facebook) require a logged-in session to access group posts. We might store cookies securely, or use official APIs if available.

- **Scheduling & Monitoring**:  
  - Use cron jobs or an external scheduler (e.g., Airflow, or a Dockerized approach) to run scrapers regularly.  
  - Log errors and maintain robust monitoring (e.g., via Slack notifications or Grafana dashboards).

- **Compliance & Privacy**:  
  - Respect site TOS and robots.txt where required.  
  - Provide unsubscribe or removal options if you contact potential leads.

---

**Summary**  
This plan outlines the real data sources, the critical data points, and a robust database approach (PostgreSQL on a cloud service). We’ll incorporate rotating proxies, possible headless browsing, and NLP-based text filtering to ensure we capture **only high-quality leads** truly interested in Naples Airbnb investments.


