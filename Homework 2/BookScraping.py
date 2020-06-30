import requests;
import pandas as pd
import time;
from scrapy.http import TextResponse;

#article[class="product_pod"] h3 a::attr(title) - Title 
#.product_pod>.One, .Two, etc. - Gets the number of stars 
#.price_color - Price with Â
#article[class="product_pod"] h3 a::attr(href) - Book link
#img::attr(src) - Image link
#..instock - Availability 

URL = "http://books.toscrape.com/"

temp_URL = "http://books.toscrape.com/"

class Book:

    def __init__(self,URL):
        self.URL = URL
        self.page = requests.get(self.URL)
        self.response = TextResponse(body=self.page.text,url=self.URL,encoding="utf-8")

    def scrape_book(self):
        "Scrapes the book with all its info."
        title = self.response.css('article[class="product_pod"] h3 a::attr(title)').extract()
        rating = self.response.css('p[class*="star-rating"]::attr(class)').extract()
        rating = [i.replace('star-rating','').strip() for i in rating]
        price = self.response.css(".price_color::text").extract()
        price = [i.replace('Â£','') for i in price]
        book_url = [URL+i for i in self.response.css('article[class="product_pod"] h3 a::attr(href)').extract()]
        img_url = [URL+i for i in self.response.css('img::attr(src)').extract()]
        in_stock = self.response.css('.instock::text').extract()
        in_stock = [i.replace('\n','').strip() for i in in_stock]
        return title, rating, price, book_url, img_url, in_stock[1::2]

    def get_next(self):
        next_url = self.response.css("li.next a::attr(href)").extract()
        return next_url



b = Book(URL)
books = []

#While a NEXT button exists, the loop will scrape everything from the page, transform the URL into the hyperlink underneath the NEXT button and continue. If no NEXT button exists, the loop will scrape the page and finish the sequence.

while True:
    #time.sleep(2)
    if(b.get_next() == []):
        books.append(b.scrape_book())
        break
    else:
        books.append(b.scrape_book())
        u = b.get_next()[0].replace('catalogue/','')
        URL = temp_URL + 'catalogue/' + u
        b = Book(URL)

#All the results are stored in "books"

print(books)