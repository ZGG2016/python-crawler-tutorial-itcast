# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class SpiderScrapyTencentPipeline:

    def __init__(self):
        self.file = open('tencent.json','wb')

    def process_item(self,item,spider):
        content = json.dumps(dict(item),ensure_ascii=False) +"\n"
        self.file.write(content.encode("utf-8"))
        return item

    def close_spider(self,spider):
        self.file.close()
