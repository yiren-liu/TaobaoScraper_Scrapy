# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass




class PhoneItem(scrapy.Item):
    num_id=Field()
    act=Field()
    area=Field()
    shopid=Field()
    auctionURL=Field()
    auctionURL_1=Field()
    auctionURL_2=Field()
    name=Field()
    nick=Field()
    originalPrice=Field()
    price=Field()
    pic_path=Field()
    pic_name=Field()
    zkType=Field()
    f_Rate=Field()
    D_Rate=Field()
    A_Rate=Field()
    S_Rate=Field()
    D_Compared=Field()
    A_Compared=Field()
    S_Compared=Field()


class MobilecaseItem(scrapy.Item):
    num_id=Field()
    act=Field()
    area=Field()
    shopid=Field()
    auctionURL=Field()
    auctionURL_1=Field()
    auctionURL_2=Field()
    name=Field()
    nick=Field()
    originalPrice=Field()
    price=Field()
    pic_path=Field()
    pic_name=Field()
    zkType=Field()
    f_Rate=Field()
    D_Rate=Field()
    A_Rate=Field()
    S_Rate=Field()
    D_Compared=Field()
    A_Compared=Field()
    S_Compared=Field()

class ComputerItem(scrapy.Item):
    num_id=Field()
    act=Field()
    area=Field()
    shopid=Field()
    auctionURL=Field()
    auctionURL_1=Field()
    auctionURL_2=Field()
    name=Field()
    nick=Field()
    originalPrice=Field()
    price=Field()
    pic_path=Field()
    pic_name=Field()
    zkType=Field()
    f_Rate=Field()
    D_Rate=Field()
    A_Rate=Field()
    S_Rate=Field()
    D_Compared=Field()
    A_Compared=Field()
    S_Compared=Field()

class MugItem(scrapy.Item):
    num_id=Field()
    act=Field()
    area=Field()
    shopid=Field()
    auctionURL=Field()
    auctionURL_1=Field()
    auctionURL_2=Field()
    name=Field()
    nick=Field()
    originalPrice=Field()
    price=Field()
    pic_path=Field()
    pic_name=Field()
    zkType=Field()
    f_Rate=Field()
    D_Rate=Field()
    A_Rate=Field()
    S_Rate=Field()
    D_Compared=Field()
    A_Compared=Field()
    S_Compared=Field()





