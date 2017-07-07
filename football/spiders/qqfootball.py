# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader

from football.items import FootballTeamItem, MatchItem


class QqfootballSpider(CrawlSpider):
    name = 'qqfootball'
    allowed_domains = ['sports.qq.com']
    start_urls = ['http://sports.qq.com/soccerdata/index.htm']

    rules = (
        Rule(LinkExtractor(allow=r'http://sports.qq.com/d/f_teams'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        teamItem = FootballTeamItem()
        teamItem['name'] = response.xpath('//h2[@class="team-logo"]/strong/text()').get()

        teamHeader = response.xpath('//div[contains(@class, "intro-con team-con")]')
        teamItem['league']  = teamHeader.xpath('.//tr[1]/td[1]/a/text()').get()
        teamItem['city']    =  teamHeader.xpath('.//tr[1]/td[2]/text()').get()
        teamItem['coach']   =  teamHeader.xpath('.//tr[1]/td[3]/text()').get()
        teamItem['start']   =  teamHeader.xpath('.//tr[2]/td[1]/text()').get()
        teamItem['court']   =  teamHeader.xpath('.//tr[2]/td[2]/text()').get()

        teamItem['matches'] = []
        for (match, attack, defense) in zip(response.xpath('//*[@id="table22_con_0"]/table/tbody/tr'),
                                            response.xpath('//*[@id="table22_con_1"]/table/tbody/tr'),
                                            response.xpath('//*[@id="table22_con_2"]/table/tbody/tr'),):
            mi = MatchItem()
            mi['date']      = match.xpath('.//td[1]/text()').get()
            mi['compet']    = match.xpath('.//td[2]/text()').get()
            mi['game']      = match.xpath('.//td[3]/a/text()').get()
            mi['result']    = match.xpath('.//td[4]/text()').get()
            mi['goal']      = match.xpath('.//td[5]/text()').get()
            mi['lose']      = match.xpath('.//td[6]/text()').get()
            mi['assist']    = match.xpath('.//td[7]/text()').get()
            mi['passball']  = match.xpath('.//td[8]/text()').get()
            mi['steal']     = match.xpath('.//td[9]/text()').get()
            mi['offside']   = match.xpath('.//td[10]/text()').get()
            mi['foul']      = match.xpath('.//td[11]/text()').get()
            mi['red']       = match.xpath('.//td[12]/text()').get()
            mi['yellow']    = match.xpath('.//td[13]/text()').get()

            mi['shoot']     = attack.xpath('.//td[4]/text()').get()
            mi['targetShoot']= attack.xpath('.//td[5]/text()').get()

            mi['targetRate']= attack.xpath('.//td[6]/text()').get()

            mi['successRate']= attack.xpath('.//td[7]/text()').get()

            mi['headScore']= attack.xpath('.//td[8]/text()').get()

            mi['directFree']= attack.xpath('.//td[9]/text()').get()

            mi['penaltyKick']= attack.xpath('.//td[10]/text()').get()

            mi['penaltyScore']= attack.xpath('.//td[11]/text()').get()


            mi['intercept']= defense.xpath('.//td[4]/text()').get()

            mi['clearance']= defense.xpath('.//td[5]/text()').get()


            mi['headClear']= defense.xpath('.//td[6]/text()').get()

            mi['backClear']= defense.xpath('.//td[7]/text()').get()

            mi['headDuel']= defense.xpath('.//td[8]/text()').get()

            mi['headDuelMiss']= defense.xpath('.//td[9]/text()').get()
            mi['ownGoal']= defense.xpath('.//td[10]/text()').get()

            teamItem['matches'].append(mi)

        return teamItem
