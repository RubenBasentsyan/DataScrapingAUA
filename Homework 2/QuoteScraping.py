import requests;
import pandas as pd
import time;
from scrapy.http import TextResponse;

URL = "http://quotes.toscrape.com/"
base_url = "http://quotes.toscrape.com"


class Quotes:

    def __init__(self,URL):
        self.URL = URL
        self.page = requests.get(self.URL)
        self.response = TextResponse(body=self.page.text,url=self.URL,encoding="utf-8")

    def get_quotes(self):
        "Gets the quotes, authors, tags and the hyperlinks to the author page"
        quotes = self.response.css("span.text::text").extract()
        authors = self.response.css("small.author::text").extract() 
        tags = [i.css("a.tag::text").extract() for i in self.response.css("div.tags")]
        hyperlinks = [base_url+i for i in self.response.css("small.author ~ a::attr(href)").extract()]
        return quotes, authors, tags, hyperlinks

    def get_next(self):
        "Transforms the URL into the next page URL, if a NEXT button exists"
        next_url = self.response.css("li.next a::attr(href)").extract()
        return next_url



quotes = []
qt = Quotes(URL)


#While a NEXT button exists, the loop will scrape everything from the page, transform the URL into the hyperlink underneath the NEXT button and continue. If no NEXT button exists, the loop will scrape the page and finish the sequence.

while True:
    time.sleep(2)
    if(qt.get_next()==[]):
        quotes.append(qt.get_quotes())
        break
    else:
        quotes.append(qt.get_quotes())
        URL = base_url + qt.get_next()[0]
        qt = Quotes(URL)


#All the results are stored in "quotes"
print(quotes)