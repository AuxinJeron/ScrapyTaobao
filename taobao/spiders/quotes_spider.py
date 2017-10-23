# coding=utf-8
from taobao.items import *

import scrapy
import json
import urllib.parse

class QuotesSpider(scrapy.Spider):
    name = "taobao_spider"
    count = 0

    def __init__(self, keyword = "test", count_limit = "1000", *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        if keyword != None:
            self.keyWord = keyword
        self.count_limit = int(count_limit)

    def start_requests(self):
        urls = [
        'https://s.taobao.com/api?_ksTS=1508637369209_219&callback=jsonp220&ajax=true&m=customized&stats_click=search_radio_all:1&q=' 
        + urllib.parse.quote(self.keyWord) +'&s=' + str(self.count) + '&imgfile=&initiative_id=staobaoz_20171022&bcoffset=0&js=1&ie=utf8&rn=975417e03cf154f7b37681821eb0c4ca',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            html = json.loads(response.body.decode().replace('}}});','}}}').replace('jsonp220(',''))
        except Exception as e:
            return 

        collection = self.keyWord.replace(' ', '_')
        for item in html['API.CustomizedApi']['itemlist']['auctions']:
            self.count = self.count + 1
            yield {
                'nid'       : item['nid'],
                'pid'       : item['pid'],
                'title'     : item['raw_title'],
                'price'     : item['view_price'],
                'category'  : item['category'],
                'seller'    : item['nick'],
                'seller_id' : item['user_id'],
                'comments'  : item['comment_count'],
                'sales'     : item['view_sales'],
                'location'  : item['item_loc'],
                'pic_url'   : item['pic_url'],
                'detail_url': item['detail_url'], 
                'collection': collection,
            }
            if self.count >= self.count_limit:
                return

        if self.count < self.count_limit : 
            new_url = 'https://s.taobao.com/api?_ksTS=1508637369209_219&callback=jsonp220&ajax=true&m=customized&stats_click=search_radio_all:1&q=' \
            + urllib.parse.quote(self.keyWord) +'&s=' + str(self.count) + '&imgfile=&initiative_id=staobaoz_20171022&bcoffset=0&js=1&ie=utf8&rn=975417e03cf154f7b37681821eb0c4ca'
            yield response.follow(new_url, callback=self.parse)






