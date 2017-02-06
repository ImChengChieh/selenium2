# -*- coding: UTF-8 -*-
from selenium import webdriver
from public import Login

login = Login()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://xktj.gongf.com/login")
driver.maximize_window()

#调用登录模快
login.user_login(driver)



#调用退出模块
login.user_logout(driver)
