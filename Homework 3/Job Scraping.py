import requests
import pandas as pd
import time;
from scrapy.http import TextResponse;

URL = "https://staff.am/en/jobs"
base_url = "https://staff.am"

#Vacancy - //div[@class="job-inner job-item-title"]/p[@class="font_bold"]/text()
#Company - //div[@class="job-inner job-item-title"]/p[@class="job_list_company_title"]/text()
#Deadline - div[class="job-inner job-list-deadline"] p::text
#Location - //div[@class="job-inner job-list-deadline"]/p[@class="job_location"]/text()
#Individual page - //div[@class="list-view"]/div/div/a/@href
#Next page - //ul[@class="pagination"]/li[@class="next"]/a/@href

class Jobs:
    def __init__(self,URL):
        self.URL = URL
        self.page = requests.get(self.URL)
        self.response = TextResponse(body=self.page.text,url=self.URL,encoding="utf-8")

    def get_vacancy(self):
        vac = self.response.xpath('//div[@class="job-inner job-item-title"]/p[@class="font_bold"]/text()').extract()
        return vac 

    def get_company(self):
        comp = self.response.xpath('//div[@class="job-inner job-item-title"]/p[@class="job_list_company_title"]/text()').extract()
        return comp

    def get_deadline(self):
        dl1 = self.response.css('div[class="job-inner job-list-deadline"] p::text').extract()
        dl2 = [''.join(x) for x in zip(dl1[0::2], dl1[1::2])]
        del dl2[1::2]
        dl = [i.replace("\n\n", "").replace("\n"," ").strip() for i in dl2]
        return dl 

    def get_location(self):
        loc = self.response.xpath('//div[@class="job-inner job-list-deadline"]/p[@class="job_location"]/text()').extract()
        loc = [i.replace('\n','').strip() for i in loc]
        return loc 

    def get_ind_page(self):
        ind_page = [base_url + i for i in self.response.xpath('//div[@class="list-view"]/div/div/a/@href').extract()]
        return ind_page

    def get_next(self):
        page = self.response.xpath('//ul[@class="pagination"]/li[@class="next"]/a/@href').extract()
        return page


j = Jobs(URL)
vacancies = []
companies = []
deadlines = []
locations = []
i_pages = []

jobs = []

while True:
    if(j.get_next() == []):
        vacancies = vacancies + j.get_vacancy()
        companies = companies + j.get_company()
        deadlines = deadlines + j.get_deadline()
        locations = locations + j.get_location()
        i_pages = i_pages + j.get_ind_page()
        break
    else:
        vacancies = vacancies + j.get_vacancy()
        companies = companies + j.get_company()
        deadlines = deadlines + j.get_deadline()
        locations = locations + j.get_location()
        i_pages = i_pages + j.get_ind_page()
        URL = base_url + j.get_next()[0]
        j = Jobs(URL)

locations = [i for i in locations if len(i)>0]

jobs.append(vacancies)
jobs.append(companies)
jobs.append(deadlines)
jobs.append(locations)
jobs.append(i_pages)

jobs = list(map(list, zip(*jobs)))
jobs_df = pd.DataFrame(jobs, columns=['Vacancies','Companies','Deadlines','Locations','Individual Pages'])
jobs_df.to_csv('jobs.csv')

fj = jobs_df['Companies'].value_counts().idxmax()
fr_comp = []
for i in jobs_df['Companies']:
    if(i == fj):
        fr_comp.append(i)


print(fj + "is the most popular company, according to the amount of jobs they have posted. As of now they have posted " + str(len(fr_comp)) + " jobs.")

jd = []
for i in jobs_df['Vacancies']:
    if("Data" in i or "DATA" in i):
        jd.append(i)

print("The word 'data' appears in exactly " + str(len(jd)) + " jobs. Those jobs are listed below.")
for i in jd:
    print(i)