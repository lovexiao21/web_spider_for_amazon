#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib2 import *
import re

#构造一个request，其中主要包含URL，Header-------------------------------------------
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
User_agent = { 'User-Agent' : user_agent }

#url = ('https://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=srs%3D1841388071%26search-alias%3Damazon-global-store&field-keywords=')
url = ('https://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=srs%3D1841388071%26search-alias%3Damazon-global-store&field-keywords=')
url2 =('https://www.amazon.cn/s/ref=sr_nr_i_0/457-5753060-5517439?fst=as%3Aoff&rh=n%3A1841388071%2Cn%3A%21152928071%2Cn%3A%21152929071%2Cn%3A1403206071%2Ci%3Ahome&bbn=1841388071&ie=UTF8&qid=1491904692')
req = Request(url2,headers=User_agent)
#----------------------------------------------------------------------------------
try:
    response = urlopen(req)

    page_info = response.read()
    pattern1 = re.compile(r'<a class="a-size-small a-link-normal a-text-normal" target="_blank" href="[^"]*"',re.M|re.I)
    reg = re.search(pattern1, page_info)
    if (reg):
        print(reg.group(0))

    f = file('D:/PycharmProjects/amazon_web_spiders/amazon_cn.txt','w')
    f.write(page_info)
    f.close()

except HTTPError,e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code:',e.code
except URLError,e:
    print 'We failed to open the URL:%s' %(url)
    print 'Reason:',e.reason
