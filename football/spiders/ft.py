# -*- coding: utf-8 -*-
import scrapy


class FtSpider(scrapy.Spider):
    name = 'ft'
    allowed_domains = ['sports.qq.com']
    start_urls = ['http://sports.qq.com/soccerdata/index.htm']

    def parse(self, response):
        with open('results/ft.html', 'w') as ft:
            ft.write(response.text)
