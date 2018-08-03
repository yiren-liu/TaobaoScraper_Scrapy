# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.items import *
import json

class TutorialPipeline(object):
    
    def __init__(self):
        self.count = 0

    def open_spider(self, spider):
        self.phone = open('Phone.json', 'a', encoding='utf-8')
        self.mug=open('Mug.json','a',encoding='utf-8')
        self.mobilecase = open('Mobilecase.json', 'a', encoding='utf-8')
        self.computer = open('Computer.json', 'a', encoding='utf-8')

    def close_spider(self, spider):
        self.phone.close()
        self.mug.close()
        self.mobilecase.close()
        self.computer.close()


    def process_item(self, item, spider):
        if isinstance(item,PhoneItem):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.phone.write(line)

        elif isinstance(item,MugItem):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.mug.write(line)

        elif isinstance(item,MobilecaseItem):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.mobilecase.write(line)

        else:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.computer.write(line)


        return item
