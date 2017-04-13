#!/usr/bin/python
# encoding: utf-8
from regular_exp import next_page_url

def get_all_pages_of_one_class(all_the_text,save_file_path,page_number):
    f = file(save_file_path, 'a')
    page_str = 'page number is ' + str(page_number) + ':'
    f.write(page_str)
    f.close()
    nextpagelink = next_page_url(all_the_text,save_file_path )
    if (nextpagelink == 0): #得到的下一页的url为空
        return 0
    #--存储page号，url
    #f = file(save_file_path,'a')

    '''f.write('page number is')
    f.write(page_number)
    f.write(':')'''
    #f.write(page_str)

    #--迭代，抓取下一页信息
    '''new_txt = url_catch(nextpagelink)
   get_all_pages_of_one_class(new_txt,save_file_path,page_number+1)'''
