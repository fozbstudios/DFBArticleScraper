# -*- coding: utf-8 -*-
import scrapy


class DfbarticleSpider(scrapy.Spider):
    name = 'dfbArticle'
    allowed_domains = ['disneyfoodblog.com']
    start_urls = ['http://disneyfoodblog.com/']

    def parse(self, response):
        pass
