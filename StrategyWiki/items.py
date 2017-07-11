# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MonsterItem(Item):
    monId = Field()
    monName = Field()
    monImg = Field()
    monLvl = Field()
    monHP = Field()
    monMP = Field()
    monPDR = Field()
    monMDR = Field()
    monEXP = Field()
