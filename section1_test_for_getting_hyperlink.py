#!/usr/bin/python
# encoding: utf-8

import re

f = file('D:/PycharmProjects/amazon_web_spiders/amazon_cn.txt','r')

try:
    all_the_text = f.read()
    #print(all_the_text)
    #patterns = re.compile(r'(?<=href=")[^"]*".*id="result_\d+".*data-asin="[^"]*"',re.M|re.I)
    #针对的是amazon.cn搜索结果页面，每页有24个商品，patter1+pattern2的模式使从列表页的html文档中获取每个商品的连接url----
    pattern1 = re.compile(r'(?<=li id="result).+?(?=</li>)', re.M | re.I | re.S)
    result = re.findall(pattern1,all_the_text)
    print(len(result))
    #print(result[0])

    pattern2 = re.compile(r'(?<=<a class="a-link-normal a-text-normal" target="_blank" href=")[^"]+(?=")',re.M | re.I)
    link1 = re.findall(pattern2,result[3])
    print('link1:',len(link1),link1)
    #--------------------------------------------------------------------------------------------------------------

    #---------------------------针对amazon.cn首页，用来抓取每一分类列表页面的url
    pattern4 = re.compile(r'(?<=<li>).+?(?=</li>)',re.M | re.I | re.S)
    link4 = re.findall(pattern4,all_the_text)
    print('link4:', len(link4))

    pattern3 = re.compile(r'(?<=href=")[^"]+?">.+?<span class="boldRefinementLink">.*?(?=</span><span)',re.M | re.I | re.S)
    f_w = file('D:/PycharmProjects/amazon_web_spiders/amazon_list.txt', 'w')
    for j in range(0,len(link4)):
        link2 = re.findall(pattern3,link4[j])
        print('link2:',len(link2))
        #--------------------------------------------------------------------------------------------------------------

        #----------------------------针对列表页面，获取下一页URL---------------------------------------------------------
        #patter4 = re.compile()
        #--------------------------------------------------------------------------------------------------------------

        '''for i in range(0,46):
            link2 = re.findall(pattern3, all_the_text)
            print i,len(link2),link2[i]
            f_w.writelines(link2[i])'''
        link2 = ['https://www.amazon.cn'+line.replace('&amp;','&') + '\n' for line in link2]
        f_w.writelines(link2)
    f_w.close()

    for i in range(0,len(result)):
        link1 = re.findall(pattern2, result[i])
        print(i,len(link1), link1)
    for i in range(0, len(link2)):
        link1 = re.findall(pattern3, all_the_text)
        print(i, len(link1), link2[i])
finally:
    f.close()