import numpy as np
import pandas as pd
import requests;
import time;
from scrapy.http import TextResponse;

URL = "http://quotes.toscrape.com/";

#page = requests.get(URL)
#response = TextResponse(body=page.text,url=URL,encoding="utf-8")

#response.css("span.text::text").extract()
#print(response.css("span.text::text").extract_first())

#def get_quotes(URL):
#    page = requests.get(URL)
#    response = TextResponse(body=page.text,url=URL,encoding="utf-8")
#    return response.css("span.text::text").extract()

#def get_authors(URL):
#    page = requests.get(URL)
#    response = TextResponse(body=page.text,url=URL,encoding="utf-8")
#    return response.css("small.author::text").extract()


class Quotes:
    def __init__(self,URL):
        self.URL = URL
        self.page = requests.get(self.URL)
        self.response = TextResponse(body=self.page.text,url=self.URL,encoding="utf-8")

    def get_quotes(self):
        return self.response.css("span.text::text").extract()

    def get_authors(self):
        return self.response.css("small.author::text").extract() 

    def get_tags(self):
        "gets the tags all in one list"
        return self.response.css("div.tags > a.tag::text").extract() 

    def get_author_link(self):
        return self.response.css("small.author ~ a::attr(href)").extract() 

page_1 = Quotes(URL)


#class Dog: 
#    legs = 4

#    def __init__(self, color, weight, age, gender, size):
#        self.color = color
#        self.weight = weight
#        self.age = age
#        self.gender = gender
#        self.size = size

#    def bark(self):
#        print("woof woof")

#    def catch_the_ball(self):
#        print(f"I cannot catch the ball, I am still {self.age} years old")

#    def catch_the_cat(self):
#        print("No")

#    def play_dead(self):
#        print("...")
        

#rex = Dog(color="brown", weight="23",age=4,gender="male",size="large")
#rex = Dog()
#print(rex.legs)
#rex.bark()
#rex.catch_the_ball()



