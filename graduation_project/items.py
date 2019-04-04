# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GraduationProjectItem(scrapy.Item):
    pass


class OriginMessageDetailItem(scrapy.Item):
    db_symbol = scrapy.Field()
    title = scrapy.Field()
    pub_time = scrapy.Field()
    pub_source = scrapy.Field()
    all_content = scrapy.Field()
    current_url = scrapy.Field()
