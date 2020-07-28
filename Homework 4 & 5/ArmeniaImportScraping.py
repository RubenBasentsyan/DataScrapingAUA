from dbnomics import fetch_series
import requests
from scrapy.http import TextResponse
import csv
import pandas as pd
import os
import matplotlib.pyplot as plt

#Dbnomics codes = //a[@class="leading-normal"]/@href
#Next button = //a[@class = "btn btn-outline"]/@href

#base_url = "https://db.nomics.world/"
#URL = "https://db.nomics.world/Eurostat/enpr_etmain"

#",".join()

#def get_codes(URL):
#    page = requests.get(URL);   
#    response = TextResponse(body=page.text,url=URL,encoding="utf-8")
#    codes = response.xpath('//a[@class="leading-normal"]/@href').extract()
#    return codes


#//table[@class="htCore"]//tr/td[2]/text() - Country codes


with open('Homework 4 & 5/data_csv.csv', newline='') as f:
    reader = csv.reader(f)
    temp_list = list(reader)

tmp_list = []
codes = []

for sublist in temp_list:
    for item in sublist:
        tmp_list.append(item)

for i in tmp_list:
    codes.append("IMF/DOT/A.AM.TMG_CIF_USD." + str(i))


dt = pd.DataFrame()
data = pd.DataFrame()


if(os.path.isfile('Homework 4 & 5/Import_Data.csv') == False):
    for i in codes:
        dt = fetch_series(str(i))
        data = data.append(dt)
        dt.iloc[0:0]
        data.to_csv("Homework 4 & 5\Import_Data.csv")

if(os.path.isfile('Homework 4 & 5/Import_Data.csv') == True):
    dtt = pd.read_csv("Homework 4 & 5/Import_Data.csv")


import_data = dtt[["original_value","original_period","Counterpart Reference Area"]]
grouped_data = import_data.groupby(['original_period']).sum()
sorted_data = grouped_data.sort_values(by="original_value", ascending = False)

grouped_country = import_data.groupby(['Counterpart Reference Area']).sum()
sorted_country = grouped_country.sort_values(by='original_value',ascending = False)

georgia = import_data.loc[import_data['Counterpart Reference Area'] == "Georgia"]
georgia.plot(x='original_period', y='original_value')

print("Armenia experienced the highest value of imports in " + str(sorted_data.index[0]))
print("The 3rd largest import partner of Armenia according to the most recent data is " + str(sorted_country.index[2]))
plt.show()