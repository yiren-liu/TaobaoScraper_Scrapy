import scrapy
import json
import re
from scrapy import Selector
from tutorial.items import *
from urllib.parse import urlencode
import yaml
import pandas as pd
import numpy as np
import requests
import time
import sys
import os
import xlsxwriter
from sys import argv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor,defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

def get_delta(lower, upper, length):
    return (upper - lower) / length

def get_date():
	a = time.strftime("%Y/%m/%d", time.localtime()).split('/')
	[year,month,date] = a
	return year,month,date

class Phonespider(scrapy.Spider):
    name = "Phonespider"
    KeysList = ['手机']
    PageNum = 20
    print(KeysList)

    start_urls = []
    for key in KeysList:
        for page in range(PageNum):
            start_urls.append('''https://s.m.taobao.com/search?event_submit_do_new_search_auction=1\
        &_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&\
        from=1&q=''' + key + '''&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=10&wlsort=10&page=''' + str(page))



    def __init__(self):
        year,month,date = get_date()
        self.html_date = year+'/'+month+'/'+date
        self.search_count=0
        self.PageNum = 20
        
    

    def parse(self, response):
        Phone_Item = PhoneItem()
        body = response.body
        dic_body = eval(body)

        for i in range(20):
            #print ("当前正在采集第 ", i + 1, " 个,第", str(self.PageNum), ' 页')
            

            Phone_Item['num_id'] = dic_body["listItem"][i]['item_id']

            Phone_Item['act'] = dic_body["listItem"][i]['act']  # 付款数

            Phone_Item['area'] = dic_body["listItem"][i]['area']  # 地区

            Phone_Item['shopid'] = dic_body["listItem"][i]['userId']  # 地区

            if dic_body["listItem"][i]['url'].find('https:') != -1:
                Phone_Item['auctionURL'] = dic_body["listItem"][i]['url']  # 商品url
            else:
                Phone_Item['auctionURL'] = "https:" + dic_body["listItem"][i]['url']  # 商品url

                # https://detail.tmall.com/item.htm?id="+str(num_id)
            # print len(auctionURL)
            if(len(Phone_Item['auctionURL']) > 250):
                Phone_Item['auctionURL_1'] = Phone_Item['auctionURL'][:250]
                Phone_Item['auctionURL_2'] = Phone_Item['auctionURL'][250::]
            else:
                Phone_Item['auctionURL_1'] = Phone_Item['auctionURL']
                Phone_Item['auctionURL_2'] = ''

            Phone_Item['name'] = dic_body["listItem"][i]['name']  # 商品名

            Phone_Item['nick'] = dic_body["listItem"][i]['nick']  # 店铺名

            Phone_Item['originalPrice'] = dic_body["listItem"][i]['originalPrice']  # 原始价格

            Phone_Item['price'] = dic_body["listItem"][i]['price']  # 当前价格

            pic_path = dic_body["listItem"][i]['pic_path']  # 当前价格
            # print pic_path
            Phone_Item['pic_path'] = pic_path.replace('60x60', '210x210')
            Phone_Item['pic_name'] = str(i + 1 + (self.PageNum - 1) * 20) + '-' + Phone_Item['name']
            #img_download(pic_name, pic_path, mkname + '/pic')

            Phone_Item['zkType'] = dic_body["listItem"][i]['zkType']  # 当前价格

           

             # 获取店铺评分

            shopcard = requests.get('https://s.taobao.com/api?sid=' + str(Phone_Item['shopid']) + '&callback=shopcard&app=api&m=get_shop_card')
            shopcard = shopcard.text.lstrip('\n\nshopcard(').rstrip(');')
            attempts=0
            success=False
            while attempts < 3 and not success:
                try:
                    #print('shopid=',shopid)
                    shopcard=eval(shopcard)
                    Phone_Item['f_Rate']=shopcard['favorableRate']
                    D_Rate=shopcard['matchDescription']
                    A_Rate=shopcard['serviceAttitude']
                    S_Rate=shopcard['deliverySpeed']
                    D_Compared=shopcard['descriptionCompared']['text']+shopcard['descriptionCompared']['rate']
                    A_Compared=shopcard['attitudeCompared']['text']+shopcard['attitudeCompared']['rate']
                    S_Compared=shopcard['deliveryCompared']['text']+shopcard['deliveryCompared']['rate']
                    success = True
                except:
                    shopcard = requests.get(
                        'https://s.taobao.com/api?sid=' + str(Phone_Item['shopid']) + '&callback=shopcard&app=api&m=get_shop_card')
                    f_Rate = []
                    D_Rate = []
                    A_Rate = []
                    S_Rate = []
                    D_Compared = []
                    A_Compared = []
                    S_Compared = []
                    print('店铺信息爬取失败！')
                    attempts += 1
                    if attempts == 3:
                        break

            yield Phone_Item

class Mugspider(scrapy.Spider):
    name = "Mugspider"
    KeysList = ['马克杯']
    PageNum = 20
    print(KeysList)

    start_urls = []
    for key in KeysList:
        for page in range(PageNum):
            start_urls.append('''https://s.m.taobao.com/search?event_submit_do_new_search_auction=1\
        &_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&\
        from=1&q=''' + key + '''&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=10&wlsort=10&page=''' + str(page))



    def __init__(self):
        year,month,date = get_date()
        self.html_date = year+'/'+month+'/'+date
        self.search_count=0
        self.PageNum = 20
        
    

    def parse(self, response):
        Mug_Item = MugItem()
        body = response.body
        dic_body = eval(body)

        for i in range(20):
            #print ("当前正在采集第 ", i + 1, " 个,第", str(self.PageNum), ' 页')
            

            Mug_Item['num_id'] = dic_body["listItem"][i]['item_id']

            Mug_Item['act'] = dic_body["listItem"][i]['act']  # 付款数

            Mug_Item['area'] = dic_body["listItem"][i]['area']  # 地区

            Mug_Item['shopid'] = dic_body["listItem"][i]['userId']  # 地区

            if dic_body["listItem"][i]['url'].find('https:') != -1:
                Mug_Item['auctionURL'] = dic_body["listItem"][i]['url']  # 商品url
            else:
                Mug_Item['auctionURL'] = "https:" + dic_body["listItem"][i]['url']  # 商品url

                # https://detail.tmall.com/item.htm?id="+str(num_id)
            # print len(auctionURL)
            if(len(Mug_Item['auctionURL']) > 250):
                Mug_Item['auctionURL_1'] = Mug_Item['auctionURL'][:250]
                Mug_Item['auctionURL_2'] = Mug_Item['auctionURL'][250::]
            else:
                Mug_Item['auctionURL_1'] = Mug_Item['auctionURL']
                Mug_Item['auctionURL_2'] = ''

            Mug_Item['name'] = dic_body["listItem"][i]['name']  # 商品名

            Mug_Item['nick'] = dic_body["listItem"][i]['nick']  # 店铺名

            Mug_Item['originalPrice'] = dic_body["listItem"][i]['originalPrice']  # 原始价格

            Mug_Item['price'] = dic_body["listItem"][i]['price']  # 当前价格

            pic_path = dic_body["listItem"][i]['pic_path']  # 当前价格
            # print pic_path
            Mug_Item['pic_path'] = pic_path.replace('60x60', '210x210')
            Mug_Item['pic_name'] = str(i + 1 + (self.PageNum - 1) * 20) + '-' + Mug_Item['name']
            #img_download(pic_name, pic_path, mkname + '/pic')

            Mug_Item['zkType'] = dic_body["listItem"][i]['zkType']  # 当前价格

            yield Mug_Item

class Mobilecasespider(scrapy.Spider):
    name = "Mobilecasespider"
    KeysList = ['手机壳']
    PageNum = 20
    print(KeysList)

    start_urls = []
    for key in KeysList:
        for page in range(PageNum):
            start_urls.append('''https://s.m.taobao.com/search?event_submit_do_new_search_auction=1\
        &_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&\
        from=1&q=''' + key + '''&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=10&wlsort=10&page=''' + str(page))



    def __init__(self):
        year,month,date = get_date()
        self.html_date = year+'/'+month+'/'+date
        self.search_count=0
        self.PageNum = 20
        
    

    def parse(self, response):
        Mobilecase_Item = MobilecaseItem()
        body = response.body
        dic_body = eval(body)

        for i in range(20):
            #print ("当前正在采集第 ", i + 1, " 个,第", str(self.PageNum), ' 页')
            

            Mobilecase_Item['num_id'] = dic_body["listItem"][i]['item_id']

            Mobilecase_Item['act'] = dic_body["listItem"][i]['act']  # 付款数

            Mobilecase_Item['area'] = dic_body["listItem"][i]['area']  # 地区

            Mobilecase_Item['shopid'] = dic_body["listItem"][i]['userId']  # 地区

            if dic_body["listItem"][i]['url'].find('https:') != -1:
                Mobilecase_Item['auctionURL'] = dic_body["listItem"][i]['url']  # 商品url
            else:
                Mobilecase_Item['auctionURL'] = "https:" + dic_body["listItem"][i]['url']  # 商品url

                # https://detail.tmall.com/item.htm?id="+str(num_id)
            # print len(auctionURL)
            if(len(Mobilecase_Item['auctionURL']) > 250):
                Mobilecase_Item['auctionURL_1'] = Mobilecase_Item['auctionURL'][:250]
                Mobilecase_Item['auctionURL_2'] = Mobilecase_Item['auctionURL'][250::]
            else:
                Mobilecase_Item['auctionURL_1'] = Mobilecase_Item['auctionURL']
                Mobilecase_Item['auctionURL_2'] = ''

            Mobilecase_Item['name'] = dic_body["listItem"][i]['name']  # 商品名

            Mobilecase_Item['nick'] = dic_body["listItem"][i]['nick']  # 店铺名

            Mobilecase_Item['originalPrice'] = dic_body["listItem"][i]['originalPrice']  # 原始价格

            Mobilecase_Item['price'] = dic_body["listItem"][i]['price']  # 当前价格

            pic_path = dic_body["listItem"][i]['pic_path']  # 当前价格
            # print pic_path
            Mobilecase_Item['pic_path'] = pic_path.replace('60x60', '210x210')
            Mobilecase_Item['pic_name'] = str(i + 1 + (self.PageNum - 1) * 20) + '-' + Mobilecase_Item['name']
            #img_download(pic_name, pic_path, mkname + '/pic')

            Mobilecase_Item['zkType'] = dic_body["listItem"][i]['zkType']  # 当前价格

            yield Mobilecase_Item

class Computerspider(scrapy.Spider):
    name = "Computerspider"
    KeysList = ['电脑']
    PageNum = 20
    print(KeysList)

    start_urls = []
    for key in KeysList:
        for page in range(PageNum):
            start_urls.append('''https://s.m.taobao.com/search?event_submit_do_new_search_auction=1\
        &_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&\
        from=1&q=''' + key + '''&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=10&wlsort=10&page=''' + str(page))



    def __init__(self):
        year,month,date = get_date()
        self.html_date = year+'/'+month+'/'+date
        self.search_count=0
        self.PageNum = 20
        
    

    def parse(self, response):
        Computer_Item = ComputerItem()
        body = response.body
        dic_body = eval(body)

        for i in range(20):
            #print ("当前正在采集第 ", i + 1, " 个,第", str(self.PageNum), ' 页')
            

            Computer_Item['num_id'] = dic_body["listItem"][i]['item_id']

            Computer_Item['act'] = dic_body["listItem"][i]['act']  # 付款数

            Computer_Item['area'] = dic_body["listItem"][i]['area']  # 地区

            Computer_Item['shopid'] = dic_body["listItem"][i]['userId']  # 地区

            if dic_body["listItem"][i]['url'].find('https:') != -1:
                Computer_Item['auctionURL'] = dic_body["listItem"][i]['url']  # 商品url
            else:
                Computer_Item['auctionURL'] = "https:" + dic_body["listItem"][i]['url']  # 商品url

                # https://detail.tmall.com/item.htm?id="+str(num_id)
            # print len(auctionURL)
            if(len(Computer_Item['auctionURL']) > 250):
                Computer_Item['auctionURL_1'] = Computer_Item['auctionURL'][:250]
                Computer_Item['auctionURL_2'] = Computer_Item['auctionURL'][250::]
            else:
                Computer_Item['auctionURL_1'] = Computer_Item['auctionURL']
                Computer_Item['auctionURL_2'] = ''

            Computer_Item['name'] = dic_body["listItem"][i]['name']  # 商品名

            Computer_Item['nick'] = dic_body["listItem"][i]['nick']  # 店铺名

            Computer_Item['originalPrice'] = dic_body["listItem"][i]['originalPrice']  # 原始价格

            Computer_Item['price'] = dic_body["listItem"][i]['price']  # 当前价格

            pic_path = dic_body["listItem"][i]['pic_path']  # 当前价格
            # print pic_path
            Computer_Item['pic_path'] = pic_path.replace('60x60', '210x210')
            Computer_Item['pic_name'] = str(i + 1 + (self.PageNum - 1) * 20) + '-' + Computer_Item['name']
            #img_download(pic_name, pic_path, mkname + '/pic')

            Computer_Item['zkType'] = dic_body["listItem"][i]['zkType']  # 当前价格

            yield Computer_Item



#configure_logging()
#process = CrawlerProcess()
#process.crawl(Phonespider)
#process.crawl(Mobilecasespider)
#process.crawl(Computerspider)
#process.crawl(Mugspider)
#process.start()
