# pipelines.py

import psycopg2
import logging

class PostgresPipeline:
    def __init__(self):
        """
        In a real production environment, you should not hardcode credentials here.
        Instead, use environment variables or a config file to store your DB connection info.
        """
        self.host = 'localhost'
        self.dbname = 'lead_generation'
        self.user = 'lead_user'
        self.password = 'Andrea#121519'  # Replace with your secure password

    def open_spider(self, spider):
        """
        Called when the spider is opened. Establishes a connection to PostgreSQL and
        ensures the table exists with the required columns (title, link, scraped_at).
        """
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()

            # Create the table if it doesn't already exist, including a 'link' column.
            create_table_query = """
                CREATE TABLE IF NOT EXISTS example_leads (
                    id SERIAL PRIMARY KEY,
                    title TEXT,
                    link TEXT,
                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()

        except Exception as e:
            logging.error(f"Error connecting to PostgreSQL: {e}")
            raise

    def close_spider(self, spider):
        """
        Called when the spider closes. Closes the DB cursor and connection.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def process_item(self, item, spider):
        """
        Called for every item Scrapy yields. Inserts the 'title' and 'link' into PostgreSQL.
        """
        try:
            insert_query = """
                INSERT INTO example_leads (title, link)
                VALUES (%s, %s)
            """
            data_tuple = (
                item.get('title'),
                item.get('link')
            )
            self.cursor.execute(insert_query, data_tuple)
            self.connection.commit()
        except Exception as e:
            logging.error(f"Error inserting item into PostgreSQL: {e}")
            self.connection.rollback()

        return item
