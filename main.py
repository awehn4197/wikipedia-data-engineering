import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from scraper.wikipedia_scraper import Scraper

if __name__ == "__main__":
  scraper = Scraper()
  page_cycle = scraper.scrape(wikipedia_page_key="Philosophy")

  scraper.convert_to_csv(scraped_data=page_cycle, wikipedia_page_key="Philosophy", data_level="bronze")