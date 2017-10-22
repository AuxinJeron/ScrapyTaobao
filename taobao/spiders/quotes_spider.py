# coding=utf-8
from taobao.items import *

import scrapy
import json
import urllib.parse

class QuotesSpider(scrapy.Spider):
    name = "taobao_spider"
    count = 0
    count_limit = 1000
    keyWord = "dior"
    start_urls = [
        'https://s.taobao.com/api?_ksTS=1508637369209_219&callback=jsonp220&ajax=true&m=customized&stats_click=search_radio_all:1&q=' 
        + urllib.parse.quote(keyWord) +'&s=' + str(count) + '&imgfile=&initiative_id=staobaoz_20171022&bcoffset=0&js=1&ie=utf8&rn=975417e03cf154f7b37681821eb0c4ca',
    ]

    def parse(self, response):
        html = json.loads(response.body.decode().replace('}}});','}}}').replace('jsonp220(',''))
        for item in html['API.CustomizedApi']['itemlist']['auctions']:
            self.count = self.count + 1
            yield {
                'title' : item['raw_title'],
                'price' : item['view_price'],
                'seller' : item['nick'],
            }

        if self.count < self.count_limit : 
            new_url = 'https://s.taobao.com/api?_ksTS=1508637369209_219&callback=jsonp220&ajax=true&m=customized&stats_click=search_radio_all:1&q=' \
            + urllib.parse.quote(self.keyWord) +'&s=' + str(self.count) + '&imgfile=&initiative_id=staobaoz_20171022&bcoffset=0&js=1&ie=utf8&rn=975417e03cf154f7b37681821eb0c4ca'
            yield response.follow(new_url, callback=self.parse)