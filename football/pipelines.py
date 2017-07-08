# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from items import FootballTeamItem

class FootballPipeline(object):
    def __init__(self):
        # self.file = codecs.open('results/matchs.json', 'w', encoding='utf-8')
        pass

    def process_item(self, item, spider):
        with codecs.open('results/team_'+item['name']+'.json', 'w', encoding='utf-8') as teamDataFile:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            teamDataFile.write(line)
        return item

    def spider_close(self, spider):
        # self.file.close()
        pass