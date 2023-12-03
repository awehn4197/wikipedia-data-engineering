
BASE_URLS = {
  "WIKIPEDIA_PAGE": "https://en.wikipedia.org/wiki/",
  "PAGE_LINK_COUNT_PAGE": "https://linkcount.toolforge.org/?project=en.wikipedia.org&page="
}

PAGE_ELEMENT_PATHS = {
  "WIKIPEDIA_ARTICLE_PAGE": {
    "PAGE_TITLE": [
      {
        "query": ["span", {"class": "mw-page-title-main"}],
        "index": 0
      }
    ],
    "SUMMARY_HTML": [
      {
        "query": ["div", {"id": "mw-content-text"}],
        "index": 0
      },
      {
        "query": ["div", {"class": "mw-parser-output"}],
        "index": 0
      },
      {
        "query": ["p", {"class": None}],
        "index": 0,
        "recursive": False
      },
    ],
    "SUMMARY_TEXT_LINKS": [
      {
        "query": ["div", {"id": "mw-content-text"}],
        "index": 0
      },
      {
        "query": ["div", {"class": "mw-parser-output"}],
        "index": 0
      },
      {
        "query": ["p", {"class": None}],
        "index": 0,
        "recursive": False
      },
      {
        "query": ["a"],
      },
    ]
  },
  "PAGE_LINK_COUNT_PAGE": {
    "NUMBER_LINKING_PAGES": [
      {
        "query": ["div", {"class": "all"}],
        "index": 0
      },
    ],
  }
}

def get_element_for_path(soup, paths):
  current_soup = soup
  for path in paths:
    recursive = path.get("recursive") or True
    index = path.get("index")
    current_soup = current_soup.find_all(*path.get("query"), recursive=recursive)
    if index is not None:
      current_soup = current_soup[index]
  return current_soup

