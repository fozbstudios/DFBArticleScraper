# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DisneyfoodblogarticlescraperPipeline(object):
    def open_spider(self, spider):
        self.file = open('articles.csv', 'w', encoding='iso-8859-1')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = item['title']+','item['url']+','+ "\n"
        self.file.write(line)
        return item
