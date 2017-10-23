# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = scrapy.Field()
    nid = scrapy.Field()
    pid = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    seller = scrapy.Field()
    seller_id = scrapy.Field()
    comments = scrapy.Field()
    sales = scrapy.Field()
    location = scrapy.Field()
    pic_url = scrapy.Field()
    detail_url = scrapy.Field()
    pass
