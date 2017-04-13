#!/usr/bin/python
# encoding: utf-8

import re

def get_items_url(all_the_text,save_file_path):
    pattern1 = re.compile(r'(?<=li id="result).+?(?=</li>)', re.M | re.I | re.S)
    result = re.findall(pattern1, all_the_text)
    print(len(result))
    # print(result[0])

    pattern2 = re.compile(r'(?<=<a class="a-link-normal a-text-normal" target="_blank" href=")[^"]+(?=")', re.M | re.I)
    f = file(save_file_path, 'a')

    for i in range(0, len(result)):
        link1 = re.findall(pattern2, result[i])
        print(i, len(link1), link1)
        f.write(link1[0])
        f.write('\n')

    f.close()

def catalog_page_url(all_the_text,save_file_path):
    pattern4 = re.compile(r'(?<=<li>).+?(?=</li>)', re.M | re.I | re.S)
    link4 = re.findall(pattern4, all_the_text)
    print('link4:', len(link4))

    pattern3 = re.compile(r'(?<=href=")[^"]+?">.+?<span class="boldRefinementLink">.*?(?=</span><span)',
                          re.M | re.I | re.S)
    f_w = file(save_file_path,'a')
    for j in range(0, len(link4)):
        link2 = re.findall(pattern3, link4[j])
        print('link2:', len(link2))
        # --------------------------------------------------------------------------------------------------------------

        # ----------------------------针对列表页面，获取下一页URL---------------------------------------------------------
        # patter4 = re.compile()
        # --------------------------------------------------------------------------------------------------------------

        link2 = ['https://www.amazon.cn' + line.replace('&amp;', '&') + '\n' for line in link2]
        f_w.writelines(link2)
    f_w.close()

def next_page_url(all_the_text,save_file_path):
    pattern5 = re.compile(r'(?<=id="pagnNextLink").*?">.*?(?=pagnNextString)', re.M | re.I|re.S)
    pattern6 = re.compile(r'(?<=href=")[^"]*(?=">)')
    f = file(save_file_path, 'a')

    link_next_page_big_range = re.findall(pattern5, all_the_text)
    #print len(link_next_page_big_range)
    if not link_next_page_big_range:
        return 0
    link_next_page = re.findall(pattern6,link_next_page_big_range[0])
    link_next_page = ['https://www.amazon.cn' + line.replace('&amp;', '&') + '\n' for line in link_next_page]
    f.writelines(link_next_page)
    f.write('\n')

    f.close()

    if not link_next_page:
        return  0

    return link_next_page[0]