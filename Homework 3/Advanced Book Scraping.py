import requests
import pandas as pd
import time;
from scrapy.http import TextResponse;


URL = "http://books.toscrape.com/"
temp_url = "http://books.toscrape.com/"

class Book:
    def __init__(self,URL):
        self.URL = URL
        self.page = requests.get(self.URL)
        self.response = TextResponse(body=self.page.text,url=self.URL,encoding="utf-8")

    def get_next(self):
        "returns the link of the following page, if it exists"
        next_url = self.response.css("li.next a::attr(href)").extract()
        return next_url

    def get_title(self):
        title = self.response.css('article[class="product_pod"] h3 a::attr(title)').extract();
        return title

    def get_rating(self):
        rating = self.response.css('p[class*="star-rating"]::attr(class)').extract()
        rating = [i.replace('star-rating','').strip() for i in rating]
        return rating 

    def get_price(self):
        price = self.response.css(".price_color::text").extract()
        price = [i.replace('Â£','') for i in price]
        return price 

    def get_book_url(self):
         book_url = [temp_url+i for i in self.response.css('article[class="product_pod"] h3 a::attr(href)').extract()]
         return book_url

    def get_img_url(self):
        img_url = [temp_url+i for i in self.response.css('.thumbnail::attr(src)').extract()]
        return img_url

    def get_inStock(self):
        in_stock = self.response.css('.instock::text').extract()
        in_stock = [i.replace('\n','').strip() for i in in_stock]
        return in_stock[1::2]

    def get_genre(self):
        book_genre = self.response.css('.breadcrumb li:nth-child(3) a::text').extract()
        return(book_genre)

    def get_desc(self):
        book_desc = self.response.xpath('//article/p/text()').extract()
        return book_desc


b = Book(URL)
titles = []
ratings = []
prices = []
book_urls =[]
img_urls =[]
in_stock = []
genres = []
descriptions = []

temp_desc = []

books = []

while True:
    if(b.get_next() == []):
        titles = titles + b.get_title()
        ratings = ratings + b.get_rating()
        prices = prices + b.get_price()
        book_urls = book_urls + b.get_book_url()
        img_urls = img_urls + b.get_img_url()
        in_stock = in_stock + b.get_inStock()
        break
    else:
        titles = titles + b.get_title()
        ratings = ratings + b.get_rating()
        prices = prices + b.get_price()
        book_urls = book_urls + b.get_book_url()
        img_urls = img_urls + b.get_img_url()
        in_stock = in_stock + b.get_inStock()
        u = b.get_next()[0].replace('catalogue/','')
        URL = temp_url + 'catalogue/' + u
        b = Book(URL)

for i in book_urls:
    if('catalogue/' not in i):
        index = str(i).index(temp_url) + len(temp_url)
        i = i[:index] + 'catalogue/' + i[index:]
    bk = Book(i)
    genres = genres + bk.get_genre()
    for k in bk.get_desc():
        temp_desc.append(str(k).strip().strip('\n'))


descriptions = [i for i in temp_desc if len(i)>0]


books.append(titles)
books.append(ratings)
books.append(prices)
books.append(book_urls)
books.append(img_urls)
books.append(in_stock)
books.append(genres)
books.append(descriptions)

books = list(map(list, zip(*books)))
books_df = pd.DataFrame(books, columns=['Titles','Ratings','Prices','Book link','Image link','Availability','Genre','Description'])
books_df.to_csv('books.csv')


price_avg = sum(map(float,prices))/len(prices)
print("The average price is " + str(price_avg))
print(books_df.sort_values(by = ["Prices"],ascending = False).head(5))
print("Based on the top 5 most expensive books, we can say the most expensive one has 'Romance' as its genre. Furthermore, only one of the top 5 most expensive books is rated 5 stars, therefore there is no big connection between the price and the rating.")