# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from StrategyWiki.items import MonsterItem

class MonsterJsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('monster.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, MonsterItem):
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        else:
            return item
