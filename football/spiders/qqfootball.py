# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.loader import ItemLoader

from football.items import FootballTeamItem


class QqfootballSpider(CrawlSpider):
    name = 'qqfootball'
    allowed_domains = ['sports.qq.com']
    start_urls = ['http://sports.qq.com/soccerdata/index.htm']

    rules = (
        Rule(LinkExtractor(allow=r'http://sports.qq.com/d/f_teams'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        teamItem = FootballTeamItem()
        teamHeader = response.xpath('//div[contains(@class, "intro-con team-con")]')
        # teamHeader = response.xpath('//div[@class="intro-con team-con"]/table/tbody')
        teamItem['name'] = response.xpath('//h2[@class="team-logo"]/strong/text()').get()


        teamItem['league'] = teamHeader.xpath('.//tr[1]/td[1]/a/text()').get()


        ft = FootballTeamItem()
        headerLoader = ItemLoader(ft, response = response)
        headerLoader.add_xpath('name',  '//h2[@class="team-logo"]/strong/text()')
        headerLoader.add_xpath('league','//div[contains(@class, "intro-con team-con")]/table/tbody/tr[1]/td[1]/a/text()')
        headerLoader.add_xpath('coach', '//div[contains(@class, "intro-con team-con")]/table/tbody/tr[1]/td[2]/text()')
        headerLoader.add_xpath('city',  '//div[contains(@class, "intro-con team-con")]/table/tbody/tr[1]/td[3]/text()')
        headerLoader.add_xpath('start', '//div[contains(@class, "intro-con team-con")]/table/tbody/tr[2]/td[1]/text()')
        headerLoader.add_xpath('court', '//div[contains(@class, "intro-con team-con")]/table/tbody/tr[2]/td[2]/text()')
        headerLoader.load_item()


        # matchs = response.xpath('//div[@id="table22_con_0"]/table/tbody/tr[1]/td[3]/a/text()').get()
        matchs = response.xpath('//div[@id="table22_con_0"]/table/tbody/tr[1]/td[3]')
        r = matchs.xpath('./a/text()').get()
        ft['name'] = 'a'
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return ft
