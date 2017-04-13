#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from urllib2 import *
'''proxies = { "http": "113.121.185.32:20057", "https": "60.17.232.195:35452")
r = requests.get("http://www.amazon.cn", proxies=proxies)
print r.text'''

import urllib2
from random import choice

enable_proxy = True
ip_list = ['180.122.89.193:43723',
'1.199.192.97:31900',
'120.32.137.53:3323',
'117.94.204.120:27336',
'113.101.137.164:29002',
'110.85.89.34:24748',
'42.54.77.217:30628',
'27.153.128.134:29994',
'42.177.131.147:27757',
'121.204.143.30:37371',
'110.81.160.108:25058',
'42.177.125.122:23767',
'125.112.204.60:49780',
'218.14.141.127:44106',
'119.114.18.127:39686',
'222.85.22.215:49515',
'125.112.193.90:28437',
'60.17.206.203:46054',
'117.30.91.17:24159',
'117.28.145.125:32555',]

proxy_ip = choice(ip_list)
print proxy_ip
proxy_handler = urllib2.ProxyHandler({"https": proxy_ip})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)
url = "http://www.baidu.com"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
User_agent = { 'User-Agent' : user_agent }
req = urllib2.Request(url, None, headers=User_agent)
Max_Num=6
for i in range(Max_Num):
    try:
        r = urllib2.urlopen(req,timeout=3).read()
        print(r)
        f = file('D:/PycharmProjects/amazon_web_spiders/proxy_test.txt','wb')
        f.write(r)
        f.close()
        break
    except urllib2.HTTPError,e:
        if i < Max_Num - 1:
            continue
        else:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code:',e.code
    except urllib2.URLError,e:
        if i < Max_Num - 1:
            continue
        else:
            print 'We failed to open the URL:%s' %(url)
            print 'Reason:',e.reason

