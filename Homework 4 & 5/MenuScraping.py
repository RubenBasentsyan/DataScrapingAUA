import re
import os
import time
import pprint
import numpy as np
import pandas as pd
from tqdm import tqdm
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
import requests
from scrapy.http import TextResponse


#//div[contains(@class, 'item ')] - All items
#//div[@class='fl list-title']/a/@title - Item names
#//span[@class='restType']/text() - All types
#//span[@class='new_list_time_block_inner']/text() - Open/Close times
#//div[@class='fl list-title']/a/@href - Links
#//div[@class="new_favorites_and_rates_block"]//text() - Ratings


class MenuScraper(scrapy.Spider):
    name = "Menu_am"
    start_urls = ["https://www.menu.am/?status=all&sort=default"]
    
    custom_settings = {
        "LOG_LEVEL": logging.WARNING,
        "FEED_FORMAT": "csv",
        "FEED_URI": "Menu_am.csv"
    }
    
    def parse(self, response):
        temp_rating = []
        rating = []
        names = []
        category = []
        time_open = []
        link = []

        blocks = response.xpath("//div[contains(@class, 'item ')]")
        names = response.xpath("//div[@class='fl list-title']/a/@title").extract()
        category = response.xpath("//span[@class='restType']/text()").extract()
        time_open = response.xpath("//span[@class='new_list_time_block_inner']/text()").extract()
        link = ["https://www.menu.am" + i for i in response.xpath("//div[@class='fl list-title']/a/@href").extract()]

        for i in blocks:
            temp_rating.append(i.xpath('div[@class="new_favorites_and_rates_block"]//text()').extract())

        for sublist in temp_rating:
            if(sublist == []):
                rating.append(0)
                continue
            rating.append(sublist[0].strip())

        for name1, category1, time_open1, link1, rating1 in zip(names, category, time_open, link, rating):
            yield {'Names': name1, 'Category': category1, 'Time_Open': time_open1, 'Link': link1, 'Rating': rating1}


if(os.path.isfile('./Menu_am.csv') == False):
    process = CrawlerProcess()
    process.crawl(MenuScraper)
    process.start()


Menu_df = pd.read_csv('Menu_am.csv')
Sorted_rating_df = Menu_df.sort_values(by = "Rating", ascending = False)
Times = Menu_df['Time_Open']


times_list = []

for i in Times:
    if(i[8:10] != ''):
        if(int(i[8:10])<=19 and int(i[8:10])>12):
            times_list.append(i)





print("The restaurants that close exactly at or sooner than 7pm are listed below.")
print(Menu_df['Names'].loc[Menu_df['Time_Open'].isin(times_list)])
print(str(len(Menu_df['Names'].loc[Menu_df['Time_Open'].isin(times_list)])) + " restaurants in total.")

print()
print("One of the categories with the top rating is " + str(Sorted_rating_df.iloc[0]['Category']))

