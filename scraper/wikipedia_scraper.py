import re
import csv
import pathlib
import logging
# import json
import requests
from bs4 import BeautifulSoup
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from helper import BASE_URLS, PAGE_ELEMENT_PATHS, get_element_for_path

# import scraper.helper

script_path = pathlib.Path(__file__).parent.resolve()

logging.basicConfig(filename="logs.log", level=logging.INFO)
# truncating log file before new run
with open("logs.log", "w"):
    pass

class Scraper:
    """
    Encapsulates all the logic for the web scraper.
    """

    def __init__(self) -> None:
        print(script_path)
        return
        
    def scrape(self, wikipedia_page_key: str) -> list:

        """
            Iterate over all wikipedia pages. Skip redirects.
        """

        """
            Start with wikipedia page, check how many other wikipedia pages link to that page
            Take the first embedded wikipedia link in the page's content and do the same thing
            Need to handle graph cycles
        """
        wikipedia_data_headers = ["article_key", "article_name", "number_of_links_to_article", "article_url", "first_link_in_summary", "summary_html"]
        wikipedia_data = []
        # initialize data headers

        # use a hash set to track which pages have been visited to avoid graph cycles
        visited_pages = set({})


        while (wikipedia_page_key is not None and wikipedia_page_key not in visited_pages):
        
        # for i in range(20):
            # if wikipedia_page_key in visited_pages:
            #     break
            visited_pages.add(wikipedia_page_key)

            wikipedia_page_url = BASE_URLS["WIKIPEDIA_PAGE"]+wikipedia_page_key
            wikipedia_page_link_count_url = BASE_URLS["PAGE_LINK_COUNT_PAGE"]+wikipedia_page_key
            

            try:
                wiki_page_resp = requests.get(wikipedia_page_url)
                wiki_page_soup = BeautifulSoup(wiki_page_resp.text, "html.parser")
                wiki_metadata_resp = requests.get(wikipedia_page_link_count_url)
                metadata_soup = BeautifulSoup(wiki_metadata_resp.text, "html.parser")
            except requests.exceptions.RequestException as e:
                logging.log(e)
            
            number_linking_pages = int(get_element_for_path(metadata_soup, PAGE_ELEMENT_PATHS["PAGE_LINK_COUNT_PAGE"]["NUMBER_LINKING_PAGES"]).text.replace(',', ''))
            wikipedia_page_title = get_element_for_path(wiki_page_soup, PAGE_ELEMENT_PATHS["WIKIPEDIA_ARTICLE_PAGE"]["PAGE_TITLE"]).text
            wikipedia_summary_html = str(get_element_for_path(wiki_page_soup, PAGE_ELEMENT_PATHS["WIKIPEDIA_ARTICLE_PAGE"]["SUMMARY_HTML"]))

            summary_text_links = get_element_for_path(wiki_page_soup, PAGE_ELEMENT_PATHS["WIKIPEDIA_ARTICLE_PAGE"]["SUMMARY_TEXT_LINKS"])

            linked_page_key = None
            for link in summary_text_links:
                if 'Help:IPA' not in link.attrs['title']:
                    linked_page_key = re.search(r"\/wiki\/(.*)", link.attrs['href']).group(1)
                    break
            wikipedia_page_key = linked_page_key

            wikipedia_data_row = (wikipedia_page_key, wikipedia_page_title, number_linking_pages, wikipedia_page_url, linked_page_key, wikipedia_summary_html)

            row_data = {}
            for i, dt in enumerate(wikipedia_data_row):
                row_data[wikipedia_data_headers[i]] = dt
            wikipedia_data.append(row_data)

            print(row_data)
            
        
        return wikipedia_data
        
    def convert_to_csv(self, scraped_data: list, wikipedia_page_key: str, data_level: str) -> None:
        """
        Converts a list of dictionaries to a csv file

        Args:
            scraped_data (list[dict]): List of dictionaries containing each page's data
            wikipedia_page_key (str): String specifiying the unique url key of the wikipedia page
            data_level (str): Signifies the level of data, ie, gold, bronze, silver
        """


        with open(f"{script_path}/../csv/{wikipedia_page_key}-{data_level}.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=scraped_data[0].keys())
            writer.writeheader()
            writer.writerows(scraped_data)


if __name__ == "__main__":
    scraper = Scraper()
    page_cycle = scraper.scrape(wikipedia_page_key="Philosophy")

    scraper.convert_to_csv(scraped_data=page_cycle, wikipedia_page_key="Philosophy", data_level="bronze")
