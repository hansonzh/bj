# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()


class CommentsItem(scrapy.Item):
    id = scrapy.Field()
    desc = scrapy.Field()


class GoodsRelateComments(scrapy.Item):
    GoodsId = scrapy.Field()
    CommentsId = scrapy.Field()
    
