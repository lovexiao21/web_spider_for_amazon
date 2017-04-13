#!/usr/bin/python
# encoding: utf-8

import re
import regular_exp
from get_all_pages_of_one_class import *

f = file('D:/PycharmProjects/amazon_web_spiders/amazon_cn.txt','r')
f2 = 'D:/PycharmProjects/amazon_web_spiders/catalog_url.txt'
all_the_text = f.read()
file_path = 'D:/PycharmProjects/amazon_web_spiders/items_url.txt'
#regular_exp.get_items_url(all_the_text,file_path)

#regular_exp.catalog_page_url(all_the_text,f2)

url = 'https://www.amazon.cn/s/ref=sr_nr_p_36_0?rnid=2040084051&rh=n%3A1841388071%2Cn%3A2016126051%2Cn%3A%212016127051%2Cn%3A813108051%2Cn%3A813272051%2Cp_36%3A2040084051&qid=1491996221&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&bbn=1841388071&low-price=126&high-price=149.99&x=7&y=10'

text =  file('D:/PycharmProjects/amazon_web_spiders/for_test_last_page.txt','r').read()
f3 = 'D:/PycharmProjects/amazon_web_spiders/all_pages.txt'
next_page = regular_exp.next_page_url(text,f3)
print('return=',next_page)

get_all_pages_of_one_class(all_the_text,f3,1)



