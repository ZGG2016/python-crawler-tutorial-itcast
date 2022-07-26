# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderScrapyTencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名
    positionName = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 所属部门
    positionApartment = scrapy.Field()
    # 职位类别
    positionType = scrapy.Field()
    # 工作内容
    positionContent = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()

