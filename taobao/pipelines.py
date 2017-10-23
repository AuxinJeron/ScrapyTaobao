# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class TaobaoPipeline(object):

    def __init__(self):
	    connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
	    self.db = connection[settings['MONGODB_DB']]
	    #self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        collection = self.db[item.get('collection')]
        collection.insert(dict(item))
        return item
