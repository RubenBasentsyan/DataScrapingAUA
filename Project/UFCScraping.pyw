import requests
import pandas as pd
import time;
from bs4 import BeautifulSoup 
from scrapy.http import TextResponse;
import re

#Fighter names xpath = //table[@class="wikitable"][i]/tbody/tr/td/a/text()
#Fighter records xpath = //table[@class="wikitable"][i]/tbody/tr/td[3]/text()
#Fighter links xpath = //table[@class="wikitable"][i]/tbody/tr/td/a/@href
#Champ names xpath = //table[@class="wikitable"][i]/caption//a/text()
#Champ records xpath = //table[@class="wikitable"][i]/caption/b/text()
#Champ link xpath = //table[@class="wikitable"][i]/caption//span/following-sibling::a/@href
#i goes from 4 to 11 included. 


#Fighter height xpath = //th[text()="Height"]/following-sibling::td/text()
#Fighter weight xpath = //th[text()="Weight"]/following-sibling::td/text()
#Fighter reach xpath = //th[text()="Reach"]/following-sibling::td/text()
#Fighter age xpath = //table[@class="infobox vcard"]//span[@class="noprint ForceAgeToShow"]/text()

#Nationality


base_url = "https://en.wikipedia.org"
url = "https://en.wikipedia.org/wiki/Ultimate_Fighting_Championship_rankings"


class Fighters:
     def __init__(self,URL):
        self.URL = URL
        self.page = requests.get(self.URL)
        self.response = TextResponse(body=self.page.text,url=self.URL,encoding="utf-8")


     def get_names(self):
         names = []
         for i in range(4,12):
             names = names + self.response.xpath(f'//table[@class="wikitable"][{i}]/tbody/tr/td/a/text()').extract()
         return names 

     def get_champ_names(self):
         c_names = []
         for i in range(4,12):
             c_names = c_names + self.response.xpath(f'//table[@class="wikitable"][{i}]/caption//a/text()').extract()
         for i in c_names:
             if(i == "Vacant"):
                 c_names.remove(i)
         return c_names 

     def get_records(self):
         records = []
         for i in range(4,12):
             records = records + self.response.xpath('//table[@class="wikitable"][' + str(i) + ']/tbody/tr/td[3]/text()').extract()
         records = [i.replace('\n','').replace('(1)','').strip() for i in records]
         return records

     def get_champ_records(self):
         c_records = []
         for i in range(4,12):
             if(i==10):
                 c_records = c_records + ["16-1"]
                 continue
             c_records = c_records + self.response.xpath('//table[@class="wikitable"][' + str(i) + ']/caption/b/text()').extract()
         c_records = [i.replace("Champion:",'').replace('(','').replace(')','').strip() for i in c_records]
         for j in range(1,4):
             for i in c_records:
                if(len(i)<=1):
                    c_records.remove(i)
         return c_records

     def get_links(self):
         links = []
         for i in range(4,12):
             links = links + self.response.xpath('//table[@class="wikitable"][' + str(i) + ']/tbody/tr/td/a/@href').extract()
         links = [base_url + i for i in links]
         return links

     def get_champ_links(self):
         c_links = []
         for i in range(4,12):
             c_links = c_links + self.response.xpath(f'//table[@class="wikitable"][{i}]/caption//span/following-sibling::a/@href').extract()
         c_links = [base_url + i for i in c_links]
         return c_links

     def get_age(self):
         age = self.response.xpath('//table[@class="infobox vcard"]//span[@class="noprint ForceAgeToShow"]/text()').extract()
         return age

     def get_height(self):
         height = self.response.xpath('//th[text()="Height"]/following-sibling::td/text()').extract()
         return height

     def get_weight(self):
         weight = self.response.xpath('//th[text()="Weight"]/following-sibling::td/text()').extract()
         return weight

     def get_reach(self):
         reach = self.response.xpath('//th[text()="Reach"]/following-sibling::td/text()').extract()
         return reach 



f = Fighters(url)
names = f.get_names() + f.get_champ_names()
records = f.get_records() + f.get_champ_records()
links = f.get_links() + f.get_champ_links()

records = [i.replace('-',' ').replace('–',' ') for i in records if len(i) > 1]

wins = []
losses = []

for i in records:
    wins.append(i[:2])
    losses.append(i[3:5])



ages = []
heights = []
weights = []
reaches = []

temp_age = []
temp_height = []
temp_height1 = []
temp_weight = []
temp_weight1 = []
temp_reach = []
temp_reach1 = []
for i in links:
    f = Fighters(i)
    temp_age.append(f.get_age())
    temp_height.append(f.get_height())
    temp_weight.append(f.get_weight())
    temp_reach.append(f.get_reach())


for sublist in temp_age:
    for item in sublist:
        ages.append(item)
   
for sublist in temp_height:
    for item in sublist:
        temp_height1.append(item)

for sublist in temp_weight:
    for item in sublist:
        temp_weight1.append(item)

for sublist in temp_reach:
    for item in sublist:
        temp_reach1.append(item)


ages = [i.replace('age\xa0','').replace('(','').replace(')','').strip() for i in ages]
ages = list(map(int, ages))

temp_height1 = [i.replace('\xa0ft','').replace('\xa0in','').replace('\xa0cm','').replace('\xa0m','').replace('(','').replace(')','').replace('.','').replace('\d','').strip() for i in temp_height1]
heights1 = [i.split() for i in temp_height1]
for sublist in heights1:
    for item in sublist:
        heights.append(item)
heights = [i for i in heights if len(i) > 2]
heights = list(map(int, heights))

temp_weight1 = [i.replace('\xa0lb','').replace('\xa0kg','').replace('\xa0st','') for i in temp_weight1]
temp_weight1 = [i.split('(')[0] for i in temp_weight1]
temp_weight1 = [i.replace('kg','').replace(')','').replace('155–170','155').strip() for i in temp_weight1]
w = []
for i in temp_weight1:
    if(len(i)<1):
        w.append('155')
        continue
    w.append(i)
w = list(map(float, w))
for i in w:
    if(i == 112.0):
        weights.append(112.0 * 2.2)
        continue
    if(i < 100):
        weights.append(i * 2.2)
        continue
    weights.append(i)
weights = list(map(int, weights))


temp_reach1 = [i.replace('\xa0in','').replace('\xa0cm','').replace('(','').replace(')','').replace('in','').replace('m','') for i in temp_reach1]
reach1 = [i.split() for i in temp_reach1]
for sublist in reach1:
    for item in sublist:
        reaches.append(item)
reaches = [i for i in reaches if len(i) > 2]
r = list(map(float, reaches))
r1 = list(map(int, r))
reaches.clear()
for i in r1:
  if(i==1):
    r1.remove(i)
    continue
  if(i<100):
    reaches.append(i*2.54)
    continue
  reaches.append(i)
reaches = list(map(int, reaches))


fighters = []
fighters.append(names)
fighters.append(wins)
fighters.append(losses)
fighters.append(links)
fighters.append(ages)
fighters.append(weights)
fighters.append(heights)
fighters.append(reaches)


fighters = list(map(list, zip(*fighters)))
fighters_df = pd.DataFrame(fighters, columns=['Name','Wins','Losses','Link','Age','Weight(lbs)','Height(cm)','Reach(cm)'])
fighters_df.to_csv('Project/fighters.csv')



