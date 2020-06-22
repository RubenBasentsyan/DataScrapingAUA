#names = ["Stipe", "Jon", "Israel", "Kamaru", "Khabib", "Alex", "Jose", "Henry"];
#print(names[::-1]); 
#first_name = "max";
#short_names = [i[:2] for i in names];
#print(short_names);

import requests;
import time;
from scrapy.http import TextResponse;

URL = "http://quotes.toscrape.com/";
page = requests.get(URL);

#response = TextResponse(body=page.text, url=URL,encoding="utf-8");
#print(response.css("small.author::text").extract());
#for x in response.css("span.text::text").extract():
#    print(x);


#def quote_scraper(aURL):
#    requests.get(aURL);
#    response = TextResponse(body=page.text, url=URL,encoding="utf-8");
#    quotes = response.css("span.text::text").extract();
#    authors = response.css("small.author::text").extract();
#    tags = [i.css("a.tag::text").extract() for i in response.css("div.tags")];
#    return quotes, authors, tags;


def quote_scraper(URL):
  page = requests.get(URL)
  response = TextResponse(body=page.text,url=URL,encoding="utf-8")
  quotes = response.css("span.text::text").extract()
  authors = response.css("small.author::text").extract()
  tags = [i.css("a.tag::text").extract() for i in response.css("div.tags")]
  return quotes, authors, tags

time.sleep(2);

result = [quote_scraper(f"http://quotes.toscrape.com/page/{i}/") for i in range(1,6)]

for i in range(1,6):
    print(quote_scraper(f"http://quotes.toscrape.com/page/{i}/"))
  
#print(result)
