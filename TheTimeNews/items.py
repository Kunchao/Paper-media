# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThetimenewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_head = scrapy.Field()
    news_data = scrapy.Field()
    news_author = scrapy.Field()
    news_body = scrapy.Field()
    news_link = scrapy.Field()
    pass
