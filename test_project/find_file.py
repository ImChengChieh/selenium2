# -*- coding: UTF-8 -*-
import os

#定义文件目录
result_dir = 'F:\\Selenium\\test_project\\report'       #定义测试文件报告目录
lists = os.listdir(result_dir)                          #os.listdir获取目录下所有文件及文件夹

#重新按时间对目录下的文件进行排序
lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn))
print (('最新的文件夹为:' + lists[-1]))
file = os.path.join(result_dir,lists[-1])
print (file)
