# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os.pathpath
import os

class ScrapeAmazonreviewsPipeline:
    def process_item(self, item, spider):
        return item
    # def open_spider(self,spider):
    #     if os.path.isfile("output.csv") == True:
    #         os.system("del output.csv")
        