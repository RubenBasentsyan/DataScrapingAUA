import re
import time
import pprint
import numpy as np
import pandas as pd
from tqdm import tqdm
import logging
import scrapy
import requests
from scrapy.http import TextResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from itertools import combinations


options = Options()
options.headless = True

PATH = r"C:\Users\basen\Desktop\chromedriver"

ADD = "http://rate.am/en/armenian-dram-exchange-rates/central-bank-armenia"
browser = webdriver.Chrome(PATH)
browser.get(ADD)
time.sleep(3)
eur = browser.find_element_by_xpath('//select[@name="ctl00$Content$dlCurrency"]/option[@value="EUR"]')
eur.click()
time.sleep(3)
page = browser.page_source
response_1 = TextResponse(body = page, url = ADD, encoding = "utf-8")

Year = ["2018", "2019", "2020"]

Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if response_1.xpath('//select[@name="ctl00$Content$dlCurrency"]/option[@selected="selected"][@value="EUR"]'):

    for i in Year:

        print(f"Scraping Year {i}")

        year = browser.find_element_by_xpath(f'//select[@name="ctl00$Content$dlYear"]/option[@value={i}]')
        year.click()
        time.sleep(5)
        page = browser.page_source
        response = TextResponse(body = page, url = ADD, encoding = "utf-8")

        if response.xpath(f'//select[@name="ctl00$Content$dlYear"]/option[@selected="selected"][@value="{i}"]') and response_1.xpath('//select[@name="ctl00$Content$dlCurrency"]/option[@selected="selected"][@value="EUR"]'):

            Days_18 = []
            Jan_18 = []
            Feb_18 = []
            March_18  = []
            April_18 = []
            May_18 = []
            June_18 = []
            July_18 = []
            Aug_18 = []
            Sept_18 = []
            Octob_18 = []
            Nov_18 = []
            Dec_18 = []

            Days_19 = []
            Jan_19 = []
            Feb_19  = []
            March_19  = []
            April_19 = []
            May_19 = []
            June_19 = []
            July_19 = []
            Aug_19 = []
            Sept_19 = []
            Octob_19 = []
            Nov_19 = []
            Dec_19 = []

            Days_20 = []
            Jan_20 = []
            Feb_20  = []
            March_20  = []
            April_20 = []
            May_20 = []
            June_20 = []
            July_20 = []
            Aug_20 = []
            Sept_20 = []
            Octob_20 = []
            Nov_20 = []
            Dec_20 = []

            for j in range (2,33):

                days = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[1]/text()").extract()
                days = days[0].strip()

                jan_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[2]/text()").extract()
                jan = ' '.join([str(elem) for elem in jan_h])
                jan = jan.strip()

                feb_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[3]/text()").extract()
                feb = ' '.join([str(elem) for elem in feb_h])
                feb = feb.strip()

                march_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[4]/text()").extract()
                march = ' '.join([str(elem) for elem in march_h])
                march = march.strip()

                april_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[5]/text()").extract()
                april = ' '.join([str(elem) for elem in april_h])
                april = april.strip()

                may_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[6]/text()").extract()
                may = ' '.join([str(elem) for elem in may_h])
                may = may.strip()

                june_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[7]/text()").extract()
                june = ' '.join([str(elem) for elem in june_h])
                june = june.strip()

                july_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[8]/text()").extract()
                july = ' '.join([str(elem) for elem in july_h])
                july = july.strip()

                aug_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[9]/text()").extract()
                aug = ' '.join([str(elem) for elem in aug_h])
                aug = aug.strip()

                sept_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[10]/text()").extract()
                sept = ' '.join([str(elem) for elem in sept_h])
                sept = sept.strip()

                octob_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[11]/text()").extract()
                octob = ' '.join([str(elem) for elem in octob_h])
                octob = octob.strip()

                nov_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[12]/text()").extract()
                nov = ' '.join([str(elem) for elem in nov_h])
                nov = nov.strip()

                dec_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[13]/text()").extract()
                dec = ' '.join([str(elem) for elem in dec_h])
                dec = dec.strip()


                if i == "2018":
                    Days_18.append(days)
                    Jan_18.append(jan)
                    Feb_18.append(feb)
                    March_18.append(march)
                    April_18.append(april)
                    May_18.append(may)
                    June_18.append(june)
                    July_18.append(july)
                    Aug_18.append(aug)
                    Sept_18.append(sept)
                    Octob_18.append(octob)
                    Nov_18.append(nov)
                    Dec_18.append(dec)

                    EUR_18 = pd.DataFrame({
                        "Days": Days_18,
                        "January": Jan_18,
                        "February": Feb_18,
                        "March": March_18,
                        "April": April_18,
                        "May": May_18,
                        "June": June_18,
                        "July": July_18,
                        "August": Aug_18,
                        "September": Sept_18,
                        "October": Octob_18,
                        "November": Nov_18,
                        "December": Dec_18
                    })

                if i == "2019":
                    Days_19.append(days)
                    Jan_19.append(jan)
                    Feb_19.append(feb)
                    March_19.append(march)
                    April_19.append(april)
                    May_19.append(may)
                    June_19.append(june)
                    July_19.append(july)
                    Aug_19.append(aug)
                    Sept_19.append(sept)
                    Octob_19.append(octob)
                    Nov_19.append(nov)
                    Dec_19.append(dec)

                    EUR_19 = pd.DataFrame({
                        "Days": Days_19,
                        "January": Jan_19,
                        "February": Feb_19,
                        "March": March_19,
                        "April": April_19,
                        "May": May_19,
                        "June": June_19,
                        "July": July_19,
                        "August": Aug_19,
                        "September": Sept_19,
                        "October": Octob_19,
                        "November": Nov_19,
                        "December": Dec_19
                    })

                if i == "2020":
                    Days_20.append(days)
                    Jan_20.append(jan)
                    Feb_20.append(feb)
                    March_20.append(march)
                    April_20.append(april)
                    May_20.append(may)
                    June_20.append(june)
                    July_20.append(july)
                    Aug_20.append(aug)
                    Sept_20.append(sept)
                    Octob_20.append(octob)
                    Nov_20.append(nov)
                    Dec_20.append(dec)

                    EUR_20 = pd.DataFrame({
                        "Days": Days_20,
                        "January": Jan_20,
                        "February": Feb_20,
                        "March": March_20,
                        "April": April_20,
                        "May": May_20,
                        "June": June_20,
                        "July": July_20,
                        "August": Aug_20,
                        "September": Sept_20,
                        "October": Octob_20,
                        "November": Nov_20,
                        "December": Dec_20
                    })
        else:
            eur = browser.find_element_by_xpath('//select[@name="ctl00$Content$dlCurrency"]/option[@value="EUR"]')
            eur.click()
            time.sleep(3)
            year = browser.find_element_by_xpath(f'//select[@name="ctl00$Content$dlYear"]/option[@value={i}]')
            year.click()
            time.sleep(5)
            page = browser.page_source
            response = TextResponse(body = page, url = ADD, encoding = "utf-8")

            Days_18 = []
            Jan_18 = []
            Feb_18 = []
            March_18  = []
            April_18 = []
            May_18 = []
            June_18 = []
            July_18 = []
            Aug_18 = []
            Sept_18 = []
            Octob_18 = []
            Nov_18 = []
            Dec_18 = []

            Days_19 = []
            Jan_19 = []
            Feb_19  = []
            March_19  = []
            April_19 = []
            May_19 = []
            June_19 = []
            July_19 = []
            Aug_19 = []
            Sept_19 = []
            Octob_19 = []
            Nov_19 = []
            Dec_19 = []

            Days_20 = []
            Jan_20 = []
            Feb_20  = []
            March_20  = []
            April_20 = []
            May_20 = []
            June_20 = []
            July_20 = []
            Aug_20 = []
            Sept_20 = []
            Octob_20 = []
            Nov_20 = []
            Dec_20 = []

            for j in range (2,33):

                days = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[1]/text()").extract()
                days = days[0].strip()

                jan_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[2]/text()").extract()
                jan = ' '.join([str(elem) for elem in jan_h])
                jan = jan.strip()

                feb_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[3]/text()").extract()
                feb = ' '.join([str(elem) for elem in feb_h])
                feb = feb.strip()

                march_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[4]/text()").extract()
                march = ' '.join([str(elem) for elem in march_h])
                march = march.strip()

                april_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[5]/text()").extract()
                april = ' '.join([str(elem) for elem in april_h])
                april = april.strip()

                may_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[6]/text()").extract()
                may = ' '.join([str(elem) for elem in may_h])
                may = may.strip()

                june_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[7]/text()").extract()
                june = ' '.join([str(elem) for elem in june_h])
                june = june.strip()

                july_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[8]/text()").extract()
                july = ' '.join([str(elem) for elem in july_h])
                july = july.strip()

                aug_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[9]/text()").extract()
                aug = ' '.join([str(elem) for elem in aug_h])
                aug = aug.strip()

                sept_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[10]/text()").extract()
                sept = ' '.join([str(elem) for elem in sept_h])
                sept = sept.strip()

                octob_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[11]/text()").extract()
                octob = ' '.join([str(elem) for elem in octob_h])
                octob = octob.strip()

                nov_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[12]/text()").extract()
                nov = ' '.join([str(elem) for elem in nov_h])
                nov = nov.strip()

                dec_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[13]/text()").extract()
                dec = ' '.join([str(elem) for elem in dec_h])
                dec = dec.strip()


                if i == "2018":
                    Days_18.append(days)
                    Jan_18.append(jan)
                    Feb_18.append(feb)
                    March_18.append(march)
                    April_18.append(april)
                    May_18.append(may)
                    June_18.append(june)
                    July_18.append(july)
                    Aug_18.append(aug)
                    Sept_18.append(sept)
                    Octob_18.append(octob)
                    Nov_18.append(nov)
                    Dec_18.append(dec)

                    EUR_18 = pd.DataFrame({
                        "Days": Days_18,
                        "January": Jan_18,
                        "February": Feb_18,
                        "March": March_18,
                        "April": April_18,
                        "May": May_18,
                        "June": June_18,
                        "July": July_18,
                        "August": Aug_18,
                        "September": Sept_18,
                        "October": Octob_18,
                        "November": Nov_18,
                        "December": Dec_18
                    })

                if i == "2019":
                    Days_19.append(days)
                    Jan_19.append(jan)
                    Feb_19.append(feb)
                    March_19.append(march)
                    April_19.append(april)
                    May_19.append(may)
                    June_19.append(june)
                    July_19.append(july)
                    Aug_19.append(aug)
                    Sept_19.append(sept)
                    Octob_19.append(octob)
                    Nov_19.append(nov)
                    Dec_19.append(dec)

                    EUR_19 = pd.DataFrame({
                        "Days": Days_19,
                        "January": Jan_19,
                        "February": Feb_19,
                        "March": March_19,
                        "April": April_19,
                        "May": May_19,
                        "June": June_19,
                        "July": July_19,
                        "August": Aug_19,
                        "September": Sept_19,
                        "October": Octob_19,
                        "November": Nov_19,
                        "December": Dec_19
                    })

                if i == "2020":
                    Days_20.append(days)
                    Jan_20.append(jan)
                    Feb_20.append(feb)
                    March_20.append(march)
                    April_20.append(april)
                    May_20.append(may)
                    June_20.append(june)
                    July_20.append(july)
                    Aug_20.append(aug)
                    Sept_20.append(sept)
                    Octob_20.append(octob)
                    Nov_20.append(nov)
                    Dec_20.append(dec)

                    EUR_20 = pd.DataFrame({
                        "Days": Days_20,
                        "January": Jan_20,
                        "February": Feb_20,
                        "March": March_20,
                        "April": April_20,
                        "May": May_20,
                        "June": June_20,
                        "July": July_20,
                        "August": Aug_20,
                        "September": Sept_20,
                        "October": Octob_20,
                        "November": Nov_20,
                        "December": Dec_20
                    })
else:
    eur = browser.find_element_by_xpath('//select[@name="ctl00$Content$dlCurrency"]/option[@value="EUR"]')
    eur.click()
    time.sleep(3)
    
    for i in Year:

        print(f"Scraping Year {i}")

        year = browser.find_element_by_xpath(f'//select[@name="ctl00$Content$dlYear"]/option[@value={i}]')
        year.click()
        time.sleep(5)
        page = browser.page_source
        response = TextResponse(body = page, url = ADD, encoding = "utf-8")

        if response.xpath(f'//select[@name="ctl00$Content$dlYear"]/option[@selected="selected"][@value="{i}"]'):

            Days_18 = []
            Jan_18 = []
            Feb_18 = []
            March_18  = []
            April_18 = []
            May_18 = []
            June_18 = []
            July_18 = []
            Aug_18 = []
            Sept_18 = []
            Octob_18 = []
            Nov_18 = []
            Dec_18 = []

            Days_19 = []
            Jan_19 = []
            Feb_19  = []
            March_19  = []
            April_19 = []
            May_19 = []
            June_19 = []
            July_19 = []
            Aug_19 = []
            Sept_19 = []
            Octob_19 = []
            Nov_19 = []
            Dec_19 = []

            Days_20 = []
            Jan_20 = []
            Feb_20  = []
            March_20  = []
            April_20 = []
            May_20 = []
            June_20 = []
            July_20 = []
            Aug_20 = []
            Sept_20 = []
            Octob_20 = []
            Nov_20 = []
            Dec_20 = []

            for j in range (2,33):

                days = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[1]/text()").extract()
                days = days[0].strip()

                jan_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[2]/text()").extract()
                jan = ' '.join([str(elem) for elem in jan_h])
                jan = jan.strip()

                feb_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[3]/text()").extract()
                feb = ' '.join([str(elem) for elem in feb_h])
                feb = feb.strip()

                march_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[4]/text()").extract()
                march = ' '.join([str(elem) for elem in march_h])
                march = march.strip()

                april_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[5]/text()").extract()
                april = ' '.join([str(elem) for elem in april_h])
                april = april.strip()

                may_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[6]/text()").extract()
                may = ' '.join([str(elem) for elem in may_h])
                may = may.strip()

                june_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[7]/text()").extract()
                june = ' '.join([str(elem) for elem in june_h])
                june = june.strip()

                july_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[8]/text()").extract()
                july = ' '.join([str(elem) for elem in july_h])
                july = july.strip()

                aug_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[9]/text()").extract()
                aug = ' '.join([str(elem) for elem in aug_h])
                aug = aug.strip()

                sept_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[10]/text()").extract()
                sept = ' '.join([str(elem) for elem in sept_h])
                sept = sept.strip()

                octob_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[11]/text()").extract()
                octob = ' '.join([str(elem) for elem in octob_h])
                octob = octob.strip()

                nov_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[12]/text()").extract()
                nov = ' '.join([str(elem) for elem in nov_h])
                nov = nov.strip()

                dec_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[13]/text()").extract()
                dec = ' '.join([str(elem) for elem in dec_h])
                dec = dec.strip()


                if i == "2018":
                    Days_18.append(days)
                    Jan_18.append(jan)
                    Feb_18.append(feb)
                    March_18.append(march)
                    April_18.append(april)
                    May_18.append(may)
                    June_18.append(june)
                    July_18.append(july)
                    Aug_18.append(aug)
                    Sept_18.append(sept)
                    Octob_18.append(octob)
                    Nov_18.append(nov)
                    Dec_18.append(dec)

                    EUR_18 = pd.DataFrame({
                        "Days": Days_18,
                        "January": Jan_18,
                        "February": Feb_18,
                        "March": March_18,
                        "April": April_18,
                        "May": May_18,
                        "June": June_18,
                        "July": July_18,
                        "August": Aug_18,
                        "September": Sept_18,
                        "October": Octob_18,
                        "November": Nov_18,
                        "December": Dec_18
                    })

                if i == "2019":
                    Days_19.append(days)
                    Jan_19.append(jan)
                    Feb_19.append(feb)
                    March_19.append(march)
                    April_19.append(april)
                    May_19.append(may)
                    June_19.append(june)
                    July_19.append(july)
                    Aug_19.append(aug)
                    Sept_19.append(sept)
                    Octob_19.append(octob)
                    Nov_19.append(nov)
                    Dec_19.append(dec)

                    EUR_19 = pd.DataFrame({
                        "Days": Days_19,
                        "January": Jan_19,
                        "February": Feb_19,
                        "March": March_19,
                        "April": April_19,
                        "May": May_19,
                        "June": June_19,
                        "July": July_19,
                        "August": Aug_19,
                        "September": Sept_19,
                        "October": Octob_19,
                        "November": Nov_19,
                        "December": Dec_19
                    })

                if i == "2020":
                    Days_20.append(days)
                    Jan_20.append(jan)
                    Feb_20.append(feb)
                    March_20.append(march)
                    April_20.append(april)
                    May_20.append(may)
                    June_20.append(june)
                    July_20.append(july)
                    Aug_20.append(aug)
                    Sept_20.append(sept)
                    Octob_20.append(octob)
                    Nov_20.append(nov)
                    Dec_20.append(dec)

                    EUR_20 = pd.DataFrame({
                        "Days": Days_20,
                        "January": Jan_20,
                        "February": Feb_20,
                        "March": March_20,
                        "April": April_20,
                        "May": May_20,
                        "June": June_20,
                        "July": July_20,
                        "August": Aug_20,
                        "September": Sept_20,
                        "October": Octob_20,
                        "November": Nov_20,
                        "December": Dec_20
                    })
        else:
            eur = browser.find_element_by_xpath('//select[@name="ctl00$Content$dlCurrency"]/option[@value="EUR"]')
            eur.click()
            time.sleep(3)
            year = browser.find_element_by_xpath(f'//select[@name="ctl00$Content$dlYear"]/option[@value={i}]')
            year.click()
            time.sleep(5)
            page = browser.page_source
            response = TextResponse(body = page, url = ADD, encoding = "utf-8")

            Days_18 = []
            Jan_18 = []
            Feb_18 = []
            March_18  = []
            April_18 = []
            May_18 = []
            June_18 = []
            July_18 = []
            Aug_18 = []
            Sept_18 = []
            Octob_18 = []
            Nov_18 = []
            Dec_18 = []

            Days_19 = []
            Jan_19 = []
            Feb_19  = []
            March_19  = []
            April_19 = []
            May_19 = []
            June_19 = []
            July_19 = []
            Aug_19 = []
            Sept_19 = []
            Octob_19 = []
            Nov_19 = []
            Dec_19 = []

            Days_20 = []
            Jan_20 = []
            Feb_20  = []
            March_20  = []
            April_20 = []
            May_20 = []
            June_20 = []
            July_20 = []
            Aug_20 = []
            Sept_20 = []
            Octob_20 = []
            Nov_20 = []
            Dec_20 = []

            for j in range (2,33):

                days = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[1]/text()").extract()
                days = days[0].strip()

                jan_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[2]/text()").extract()
                jan = ' '.join([str(elem) for elem in jan_h])
                jan = jan.strip()

                feb_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[3]/text()").extract()
                feb = ' '.join([str(elem) for elem in feb_h])
                feb = feb.strip()

                march_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[4]/text()").extract()
                march = ' '.join([str(elem) for elem in march_h])
                march = march.strip()

                april_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[5]/text()").extract()
                april = ' '.join([str(elem) for elem in april_h])
                april = april.strip()

                may_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[6]/text()").extract()
                may = ' '.join([str(elem) for elem in may_h])
                may = may.strip()

                june_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[7]/text()").extract()
                june = ' '.join([str(elem) for elem in june_h])
                june = june.strip()

                july_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[8]/text()").extract()
                july = ' '.join([str(elem) for elem in july_h])
                july = july.strip()

                aug_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[9]/text()").extract()
                aug = ' '.join([str(elem) for elem in aug_h])
                aug = aug.strip()

                sept_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[10]/text()").extract()
                sept = ' '.join([str(elem) for elem in sept_h])
                sept = sept.strip()

                octob_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[11]/text()").extract()
                octob = ' '.join([str(elem) for elem in octob_h])
                octob = octob.strip()

                nov_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[12]/text()").extract()
                nov = ' '.join([str(elem) for elem in nov_h])
                nov = nov.strip()

                dec_h = response.xpath(f"//table[@class='cb']/tbody/tr[{j}]/td[13]/text()").extract()
                dec = ' '.join([str(elem) for elem in dec_h])
                dec = dec.strip()


                if i == "2018":
                    Days_18.append(days)
                    Jan_18.append(jan)
                    Feb_18.append(feb)
                    March_18.append(march)
                    April_18.append(april)
                    May_18.append(may)
                    June_18.append(june)
                    July_18.append(july)
                    Aug_18.append(aug)
                    Sept_18.append(sept)
                    Octob_18.append(octob)
                    Nov_18.append(nov)
                    Dec_18.append(dec)

                    EUR_18 = pd.DataFrame({
                        "Days": Days_18,
                        "January": Jan_18,
                        "February": Feb_18,
                        "March": March_18,
                        "April": April_18,
                        "May": May_18,
                        "June": June_18,
                        "July": July_18,
                        "August": Aug_18,
                        "September": Sept_18,
                        "October": Octob_18,
                        "November": Nov_18,
                        "December": Dec_18
                    })

                if i == "2019":
                    Days_19.append(days)
                    Jan_19.append(jan)
                    Feb_19.append(feb)
                    March_19.append(march)
                    April_19.append(april)
                    May_19.append(may)
                    June_19.append(june)
                    July_19.append(july)
                    Aug_19.append(aug)
                    Sept_19.append(sept)
                    Octob_19.append(octob)
                    Nov_19.append(nov)
                    Dec_19.append(dec)

                    EUR_19 = pd.DataFrame({
                        "Days": Days_19,
                        "January": Jan_19,
                        "February": Feb_19,
                        "March": March_19,
                        "April": April_19,
                        "May": May_19,
                        "June": June_19,
                        "July": July_19,
                        "August": Aug_19,
                        "September": Sept_19,
                        "October": Octob_19,
                        "November": Nov_19,
                        "December": Dec_19
                    })

                if i == "2020":
                    Days_20.append(days)
                    Jan_20.append(jan)
                    Feb_20.append(feb)
                    March_20.append(march)
                    April_20.append(april)
                    May_20.append(may)
                    June_20.append(june)
                    July_20.append(july)
                    Aug_20.append(aug)
                    Sept_20.append(sept)
                    Octob_20.append(octob)
                    Nov_20.append(nov)
                    Dec_20.append(dec)

                    EUR_20 = pd.DataFrame({
                        "Days": Days_20,
                        "January": Jan_20,
                        "February": Feb_20,
                        "March": March_20,
                        "April": April_20,
                        "May": May_20,
                        "June": June_20,
                        "July": July_20,
                        "August": Aug_20,
                        "September": Sept_20,
                        "October": Octob_20,
                        "November": Nov_20,
                        "December": Dec_20
                    })


print("Scraping Done!")
browser.close()

eur18 = EUR_18.replace("X", "NaN").replace("", "NaN")
eur19 = EUR_19.replace("X", "NaN").replace("", "NaN")

del eur18['Days']
for i in eur18:
    eur18[f"{i}"] = pd.to_numeric(eur18[f"{i}"], downcast = "float", errors='coerce')

del eur19['Days']
for i in eur19:
    eur19[f"{i}"] = pd.to_numeric(eur19[f"{i}"], downcast = "float", errors='coerce')

for i in Month:
    mdf = eur19.sub(eur18, axis = i)


print("The annual variations of exchange rate for 2018 for EUR is " + str(eur18.var().mean()))
print("The annual variations of exchange rate for 2019 for EUR is " + str(eur19.var().mean()))

print("The variation of month to month differences is " + str(mdf.var().mean()))