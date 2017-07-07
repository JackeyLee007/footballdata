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


class MatchItem(scrapy.Item):
    date = scrapy.Field()
    compet = scrapy.Field()
    game = scrapy.Field()
    result = scrapy.Field()
    goal = scrapy.Field()
    lose = scrapy.Field()
    assist = scrapy.Field()
    passball = scrapy.Field()
    steal = scrapy.Field()
    offside = scrapy.Field()
    foul = scrapy.Field()
    red = scrapy.Field()
    yellow = scrapy.Field()

    # 射门
    shoot       = scrapy.Field()
    #射正
    targetShoot = scrapy.Field()
    # 射正率
    targetRate  = scrapy.Field()
    # 成功率
    successRate = scrapy.Field()
    # 头球进球
    headScore   = scrapy.Field()
    # 直接任意球进球
    directFree  = scrapy.Field()
    # 点球
    penaltyKick = scrapy.Field()
    # 赢得点球
    penaltyScore= scrapy.Field()
    #=============================
    # 拦截
    intercept   = scrapy.Field()
    # 解围
    clearance   = scrapy.Field()
    # 头球解围
    headClear   = scrapy.Field()
    # 后场解围
    backClear   = scrapy.Field()
    # 头球争顶成功
    headDuel    = scrapy.Field()
    # 头球争顶失败
    headDuelMiss= scrapy.Field()
    # 乌龙球
    ownGoal     = scrapy.Field()


class FootballTeamItem(scrapy.Item):

    name    = scrapy.Field()
    league  = scrapy.Field()
    city    = scrapy.Field()
    court   = scrapy.Field()
    start   = scrapy.Field()
    coach   = scrapy.Field()
    matches = scrapy.Field()
