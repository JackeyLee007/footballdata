# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FootballItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FootballTeamItem(scrapy.Item):

    name    = scrapy.Field()
    league  = scrapy.Field()
    city    = scrapy.Field()
    court   = scrapy.Field()
    start   = scrapy.Field()
    coach   = scrapy.Field()
