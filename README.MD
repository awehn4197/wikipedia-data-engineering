https://lucid.app/lucidchart/f77f501d-1a5d-4bf5-b280-691a9592ff1c/edit?beaconFlowId=8DE8E57258833EB3&invitationId=inv_68b0bdf0-4f9f-4fcc-8020-f8cf8f06a2f0&page=0_0
    iterate over all wikipedia pages
    record the date of the first look at the list of pages
    later use that date to cross reference against the rss feed for new wikipedia pages
    but start capturing the rss feeds now because they might expire before we get back to them
    then start processing the rss feeds to get the summaries of new articles too
    analysts can go in and flag pages that they want specific updates from and what kind of information to collect

TODO: ESCAPE HTML STRINGS BECAUSE THEY CONTAIN BOTH SINGLE AND DOUBLE QUOTES
            
            
is there a way to give a quanitifiable metric to how "abstract" the meaning of a single word is?


now to find the first link in the wikipedia page text
this requires a definition
i'm defining it as:
the first non-pronunciation related link to another wikipedia page in the first p tag without a class attribute inside the div with class mw-parser-output inside the div with id mw-content-text
whether or not that definition will hold up or run into an exception - i'm not sure yet
but basically i'm trying to examine the summary text at the top of the article, while ignoring any "notes", disambiguations, etc.


other scraping ideas (?):
 scrape
 - petfinder.com ? track dogs up for adoption in your neighborhood, scrape id, link, name, breed, short description, image, create list of dogs up for adoption, check each day to see if they got adopted
       look for next page button to see if there are more dogs, keep loading new pages til this button is no longer seen
       dont really need to web scrape here tho - can just call the api directly
 - look up all car washes within radius of your zip code and check for deals...?

        # self.base_url = "https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version"
