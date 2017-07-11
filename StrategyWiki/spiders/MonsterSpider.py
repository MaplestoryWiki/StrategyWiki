# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from StrategyWiki.items import MonsterItem


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

class MonsterspiderSpider(scrapy.Spider):
    name = 'MonsterSpider'
    allowed_domains = ['https://strategywiki.org']
    start_urls = [
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_1-10',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_11-20',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_21-30',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_31-40',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_41-50',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_51-60',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_61-70',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_71-80',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_81-90',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_91-100',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_101-110',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_111-120',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_121-130',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_131-140',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_141-150',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_151-160',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_161-170',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_171-180',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_181-190',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_191-200',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_201-210',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_211-220',
        'https://strategywiki.org/wiki/MapleStory/Monsters/Level_221-230',
    ]

    def parse(self, response):
        page = Selector(text=response.body)
        monsList = page.xpath('//table[@class="prettytable"]/tr')

        for mon in monsList:
            try:
                monId = mon.xpath('.//td/span/@id').extract_first()
                if monId is None:
                    # skip heading
                    continue

                monName = mon.xpath('.//td/b/text()').extract_first()
                monImg = mon.xpath('.//td/a/img/@src').extract_first()

                infoName  = mon.xpath('.//td/ul/li/b/text()').extract()
                infoValue = mon.xpath('.//td/ul/li/text()').extract()

                for iName, iValue in zip(infoName,infoValue):
                    if iName.lower().strip() == 'level':
                        monLvl = safe_cast(iValue.strip(':'), int, None)
                    elif iName.lower().strip() == 'hp':
                        monHP = safe_cast(iValue.strip(':').replace(',', ''), int, None)
                    elif iName.lower().strip() == 'mp':
                        monMP = safe_cast(iValue.strip(':').replace(',', ''), int, None)
                    elif iName.lower().strip() == 'pdr':
                        monPDR = safe_cast(iValue.strip(':').strip('%').replace(',', ''), int, None)
                    elif iName.lower().strip() == 'mdr':
                        monMDR = safe_cast(iValue.strip(':').strip('%').replace(',', ''), int, None)
                    elif iName.lower().strip() == 'exp':
                        monEXP = iValue.strip(':').strip()


                yield MonsterItem(
                            monId=monId,
                            monName=monName,
                            monImg=monImg,
                            monLvl=monLvl,
                            monHP=monHP,
                            monMP=monMP,
                            monPDR=monPDR,
                            monMDR=monMDR,
                            monEXP=monEXP,
                            )
            except:
                monInfo = dict(zip(infoName, infoValue))
                monInfo['monId'] = monId
                self.logger.error(monInfo)

