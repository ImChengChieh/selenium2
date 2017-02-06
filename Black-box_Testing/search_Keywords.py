# -*- coding: UTF-8 -*-
from selenium import webdriver
import time


#参数化搜索关键字
# search_text = ['Python',u'中文','text']
#
# for text in search_text:
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get('http://www.baidu.com')
#     driver.find_element_by_xpath('//*[@id="kw"]').send_keys(text)
#     driver.find_element_by_xpath('//*[@id="su"]').click()
#     time.sleep(10)
#     driver.quit()

#读取txt文件
# user_file = open('user_info.txt','r')
# lines = user_file.readlines()
# user_file.close()
#
# for line in lines:
#     username = line.split(',')[0]
#     password = line.split(',')[1]
#     print (username,password)


#读取csv文件
# import csv #导入csv包
# #读取本地CVS文件
# date = csv.reader(open('csv_read.csv','r'))
#
# #循环输出每一行信息
# for info in date:
#    print (info)         #打印每行的信息
#    print (info[0])      #打印每行第一列








