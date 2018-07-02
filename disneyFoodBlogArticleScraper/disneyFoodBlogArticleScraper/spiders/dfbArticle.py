# -*- coutf-8 -*-
import scrapy
from datetime import date, timedelta,datetime
from disneyFoodBlogArticleScraper.items import DisneyfoodblogarticlescraperItem

class DfbarticleSpider(scrapy.Spider):
    name = 'dfbArticle'
    allowed_domains = ['disneyfoodblog.com']
    formatDate='%Y_%m_%d'
    handle_httpstatus_list = [404] # so we can add fialed urls
    def __init__(self, inFile=None):
        self.firstStageURLs=[]
        self.failedURLs=[]
        self.secondStageURLs=[]
        self.earlierDateStr='2017_03_23'#must be YYYY_MM_DD
        self.laterDateStr='2017_07_23'#must be YYYY_MM_DD

    def start_requests(self):
        d1 = datetime.strptime(self.earlierDateStr,DfbarticleSpider.formatDate).date() # start date
        d2 = datetime.strptime(self.laterDateStr,DfbarticleSpider.formatDate).date() # end date
        delta = d2 - d1         # timedelta

        for i in range(delta.days + 1): #both inclusive
            cur = d1 + timedelta(i)
            # print(cur)
            # print('')
            dateArr=cur.strftime(DfbarticleSpider.formatDate).split('_')
            self.firstStageURLs.append('http://www.disneyfoodblog.com/{}/{}/{}/'.format(*dateArr))# use all args in order

        for ur in self.firstStageURLs:
            # print(ur)
            yield scrapy.Request(url=ur, callback=self.parse)

    def parse(self, response):
        if response.status == 404:
            self.failedURLs.append(response.url)
        l=response.css("[class=entry-title] a")
        for li in l:
            item = DisneyfoodblogarticlescraperItem()
            item['title'] =li.css('::text').extract_first().replace(',','')
            item['url'] =li.css('::attr(href)').extract_first()
            yield item

    def closed(self, reason):
        with open('404list.txt', "w",encoding='utf-8') as out:
            for f in self.failedURLs:
                out.write(f+'\n')
