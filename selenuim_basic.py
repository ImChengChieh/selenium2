# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")

#通过id定位
# driver.find_element_by_id("kw").send_keys("Selenium2")
# driver.find_element_by_id("su").click()

#通过xpath绝对定位
# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[5]/div[1]/div/form/span[1]/input").send_keys("Selenium2")
# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[5]/div[1]/div/form/span[2]/input").click()

#通过xpath元素属性定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("Selenium2")
# driver.find_element_by_xpath('//*[@id="su"]').click()
# driver.quit()

#通过css定位
# driver.find_element_by_css_selector('#kw').send_keys("Selenium2")
# driver.find_element_by_css_selector('#su').click()
# driver.quit()

#用By定位元素，WebDriver统一写法,使用如下方法时需要导入By类,官方更推荐前面写法
# from selenium.webdriver.common.by import By
# driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("Selenium2")
# driver.find_element(By.CSS_SELECTOR,'#su').click()
# driver.quit()

#控制浏览器窗口大小
# print ('设置浏览器宽480、高800显示')
# driver.set_window_size(480,800)
#全屏显示
# driver.maximize_window()
# driver.quit()

#控制浏览器后退，前进

#访问百度首页
# first_url = 'http://www.baidu.com'
# print("now access %s" % (first_url))
# driver.get(first_url)
#访问新闻页面
# second_url='http://news.baidu.com'
# print("now access %s" % (second_url))
# driver.get(second_url)
# #返回到百度首页
# print("back to %s" % (first_url))
# driver.back()
# #前进到新闻页
# print('forward to %s' %(second_url))
# driver.forward()
# time.sleep(10)              #10秒后关闭
# driver.quit()


#码云登录
# driver.get("http://git.oschina.net/login")
# driver.maximize_window()
#
# print ('Before login ========================')
#
# #打印当前页面title
# title = driver.title
# print (title)
#
# #打印当前url
# now_url = driver.current_url
# print (now_url)
#
# #邮箱登录
# driver.find_element_by_xpath('//*[@id="user_login"]').clear()
# driver.find_element_by_xpath('//*[@id="user_login"]').send_keys("winston@dingtalk.com")
# driver.find_element_by_xpath('//*[@id="user_password"]').clear()
# driver.find_element_by_xpath('//*[@id="user_password"]').send_keys("zhenghuacai727.com")
# driver.find_element_by_xpath('//*[@id="new_user"]/div[5]/input').click()
#
# print ('After login ========================')
#
# #打印当前页面title
# title = driver.title
# print (title)
#
# #打印当前url
# now_url = driver.current_url
# print (now_url)
#
# #获得登录的用户名
# user = driver.find_element_by_xpath('//*[@id="git-profile"]/div/div/a').text
# print (user)
#
# time.sleep(15)
# driver.quit()

#有道翻译
# driver.maximize_window()
# driver.get("http://www.youdao.com/")
# driver.find_element_by_xpath('//*[@id="translateContent"]').send_keys('中国'.decode('utf8'))
# driver.find_element_by_xpath('//*[@id="form"]/button').submit()
# time.sleep(15)
# driver.quit()

#WebElement接口常用方法
# driver.get('https://www.baidu.com/')
# driver.maximize_window()
# #返回元素的尺寸
# size = driver.find_element_by_xpath('//*[@id="kw"]').size
# print (size)
#
# #获取元素的文本
# text = driver.find_element_by_xpath('//*[@id="cp"]').text
# print (text)
#
# #获得属性值
# attribute = driver.find_element_by_xpath('//*[@id="su"]').get_attribute('type')
# print (attribute)
#
# #返回该元素是否用户可见
# result =driver.find_element_by_xpath('//*[@id="su"]').is_displayed()
# print (result)
#
# time.sleep(15)
# driver.quit()

#鼠标悬停  move_to_element()方法与鼠标右击context_click()相同,鼠标事件需要导入ActionChaims类
# ActionChains(driver)           #调用ActionChains类并将浏览器驱动driver作为参数传入
#perform();执行所有ActionChains中存储的行为，可以理解成是对整个操作元素的提交动作
#context_click()    右击
#double_click()     双击
#drag_and_drop()       拖动
#move_to_element()  鼠标悬停
# from selenium.webdriver import ActionChains
# driver.get("https://www.baidu.com/")
# driver.maximize_window()
# above = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
# click =driver.find_element_by_xpath('//*[@id="u1"]/a[7]')
# # ActionChains(driver).move_to_element(above).perform()
# # ActionChains(driver).context_click(click).perform()  #鼠标右击
# ActionChains(driver).double_click(click).perform()   #鼠标双击
# time.sleep(15)
# driver.quit()

#设置元素等待
#1.显示等待
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver.get("http://baidu.com")
#
# element = WebDriverWait(driver,5,0.5).until(
#                         EC.presence_of_element_located((By.ID,"kw"))
#                         )
# element.send_keys("selenium")
# time.sleep(15)
# driver.quit()

#用之前学习的is_displayed来判断元素是否可见
# driver.get("http://www.baidu.com")
#
# print (time.ctime())
# for i in range(10):
#     try:
#         el = driver.find_element_by_id("kw22")
#         if el.is_displayed():
#             break
#     except:pass
#     time.sleep(1)
# else:
#     print("time out")
# driver.close()
# print(time.ctime())



# from math import sqrt       #sqrt() 方法返回数字x的平方根
# for n in range(99,81,-1):   #range（start， end， scan)，不包括end,第三个参数每次跳跃间距
#  root = sqrt(n)             #参数含义：start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
#  if root == int(root):      # end:技术到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
#   print n                   # scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
#   break                     #for/else表示for循环中if条件不满足执行else语句
# else:
#  print"Didn't find it!"


#隐式等待
# from selenium.common.exceptions import NoSuchElementException
#
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
#
# try:
#     print(time.ctime())
#     driver.find_element_by_id("kw22").send_keys('selenium')
# except NoSuchElementException as e:
#     print (e)
# finally:
#     print (time.ctime())
#     driver.quit()


#多表单切换   iframe 元素会创建包含另外一个文档的内联框架（即行内框架）
# import os
#
# file_path = 'file:///' + os.path.abspath('frame.html')
# driver.get(file_path)
#
# #如果没有id,name方法，先定位到iframe,再传给switch_to.frame()
# # xf = driver.find_element_by_xpath('//*[@id="if"]')
#
# #切换到iframe(id = 'if'),switch_to.frame()默认可以直接获取表单的id或name属性
# driver.switch_to.frame("if")
#
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
#
# driver.switch_to.parent_frame()
# time.sleep(500)
#
# driver.quit()



#多窗口切换
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
#
# #获得百度搜索窗口句柄
# search_windows = driver.current_window_handle
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_link_text('立即注册').click()
#
# #获得当前所有打开的窗口的句柄
# all_handles = driver.window_handles
#
# #进入注册窗口
# for handle in all_handles:
#     if handle != search_windows:
#         driver.switch_to.window(handle)
#         print ('now register window !')
#         driver.find_element_by_name("userName").send_keys('1234566666')
#         driver.find_element_by_name("password").send_keys('passwo44444rd')
#         time.sleep(5)
#
# #回到搜索窗口
# for handle in all_handles:
#     if handle == search_windows:
#         driver.switch_to.window(handle)
#         print('now search windosws')
#         driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_2__closeBtn"]').click()
#         driver.find_element_by_xpath('//*[@id="kw"]').send_keys("Selenium2")
#         driver.find_element_by_xpath('//*[@id="su"]').click()
#         time.sleep(5)
#
# driver.quit()



#警告框处理
# driver.implicitly_wait(10)
# driver.get('http://www.baidu.com')
# #鼠标悬停至‘设置’链接
# link = driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(link).perform()
# #打开搜索设置
# driver.find_element_by_link_text("搜索设置").click()
# #保存设置
# time.sleep(2)
# driver.find_element_by_class_name('prefpanelgo').click()
# time.sleep(2)
# #接收警告
# driver.switch_to.alert.accept()  #accept()接受现有警告框
#
# driver.quit()


#操作cookie
# driver.get('http://git.oschina.net/')
# #获得cookie的信息
# # cookie = driver.get_cookies()
# # 向cookie的name和value中添加会话信息
# driver.add_cookie({'name':'key-aaa','value':'value-bbb'})
# #遍历cookie
# for cookie in driver.get_cookies():
#     print ("%s->%s" %(cookie['name'],cookie['value']))
#
# driver.close()


#调用javascript
driver.implicitly_wait(10)
driver.get("https://www.baidu.com/")
#设置窗口大小
driver.set_window_size(700,600)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_xpath('//*[@id="su"]').click()

#通过javascript设置浏览器滚动条位置
time.sleep(5)
js="window.scrollTo(100,550);"
driver.execute_script(js)
time.sleep(15)

driver.quit()


#处理html5的视频播放
# driver.maximize_window()
# driver.get("http://xktj.gongf.com/picture_video/gather_video/2")
#
# video = driver.find_element_by_xpath('//*[@id="video_column"]/div/div[1]/video')
# #返回播放地址文件地址
# url = driver.execute_script("return arguments[0].currentSrc;",video)
# print (url)
# #播放视频
# print ("start")
# driver.execute_script("return arguments[0].play()",video)
# #播放10秒
# time.sleep(10)
# #暂停视频
# print ("stop")
# driver.execute_script("return arguments[0].pause()",video)
# time.sleep(5)
# driver.quit()


#窗口截图
# driver.get("http://www.baidu.com")
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
# driver.find_element_by_xpath('//*[@id="su"]').click()
# time.sleep(5)
#
# #截取当前窗口，并指定截图图片保存位置
# driver.get_screenshot_as_file("D:/KwDownload/baidu.png")
#
# driver.quit()

#验证码的处理
#实际开放中几种经验方法
#1.去掉验证码验证
#2.设置能验证码验证
#3.验证码识别技术      Python-tesseract是光学字符识别Tesseract OCR引擎的封装类
#4.记录cookie
#设置万能验证码
# from random import randint
# #生成一个1000到9999之间的随机整数
# verify = randint(1000,9999)
# print (u"生成随机数：%d" % verify)
#
# number = input("请输入随机数")
# print (number)
# number = int(number)
#
# if number == verify:
#     print ('登录成功')
# elif number == 9989:
#     print ('登录成功')
# else:
#     print ('验证码输入有误!')


#WebDriver原理
# import logging
# logging.basicConfig(level=logging.DEBUG)
# driver.get("http://www.baidu.com")
#
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
# driver.find_element_by_xpath('//*[@id="su"]').click()
# driver.quit()














