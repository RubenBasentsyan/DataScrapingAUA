import requests;
import pandas as pd
import time;
from scrapy.http import TextResponse;

URL = "https://www.imdb.com/chart/moviemeter/"
base_url = "https://www.imdb.com"

#td.titleColumn a - Movie titles
#.secondaryInfo:nth-child(2) - Movie Year
#.velocity - Rank -> doesn't return proper rankings therefore I will use an increment 
#.imdbRating strong = Rating. Returns only if the ranking is available 
#td.titleColumn a::attr(href) - Movie hyperlink without the base url

class Movies: 
     def __init__(self,URL):
        self.URL = URL
        self.page = requests.get(self.URL)
        self.response = TextResponse(body=self.page.text,url=self.URL,encoding="utf-8")

     def scrape_movies(self):
        "Scrapes the movies, ratings, ranks and the hyperlink"
        title = self.response.css("td.titleColumn a::text").extract()
        year = [str(i).strip('()') for i in self.response.css(".secondaryInfo:nth-child(2)::text").extract()]
        rank = []
        [rank.append(i) for i in range(1,101)]
        rating = []
        for i in self.response.css(".imdbRating"):
            rating.append(str(i.css("strong::text").extract()).strip('[]'))
        hyperlink = [base_url+i for i in self.response.css("td.titleColumn a::attr(href)").extract()]
        return title, year, rank, rating, hyperlink

#While scraping, I had to do some checks. For example whether or not a ranking exists or attaching a base URL to the movie hyperlink. 

m = Movies(URL).scrape_movies()

#After scraping all the information, I replaced the empty rankings with a "No ranking" string.
for i in range(0,100):
    if(m[3][i] == ""):
        m[3][i]="No ranking"


#In order to get the details of each movie in one element of a list, I had to transpose the scraped list. 
m = list(map(list, zip(*m)))

#Finally I put the transposed list into the DataFrame and named the columns to make it look better.
df = pd.DataFrame(m, columns=['Title','Year','Rank','Rating','Hyperlink'])
print(df)

#All the information needed is the DataFrame "df"   









