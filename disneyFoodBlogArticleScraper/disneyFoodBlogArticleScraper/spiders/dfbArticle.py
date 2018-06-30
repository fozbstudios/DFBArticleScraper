# -*- coutf-8 -*-
import scrapy
from datetime import date, timedelta,datetime

class DfbarticleSpider(scrapy.Spider):
    name = 'dfbArticle'
    allowed_domains = ['disneyfoodblog.com']
    def __init__(self, inFile=None):
        self.firstStageURLs=[]
        self.secondStageURLs=[]
        self.earlierDateStr='2017_03_23'#must be YYYY_MM_DD
        self.laterDateStr='2017_07_23'#must be YYYY_MM_DD

    def start_requests(self):
        d1 = datetime.strptime(self.earlierDateStr,'%Y_%m_%d').date() # start date
        d2 = datetime.strptime(self.laterDateStr,'%Y_%m_%d').date() # end date
        delta = d2 - d1         # timedelta

        for i in range(delta.days + 1): #both inclusive
            cur = d1 + timedelta(i)
            print(cur)
            print('')
            print(cur.split('_'))
        for ur in self.firstStageURLs:
            yield scrapy.Request(url=ur, callback=self.parse)

    def parse(self, response):
        pass
