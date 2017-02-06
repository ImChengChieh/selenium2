# -*- coding: UTF-8 -*-
import time
class Login():

    #登录
    def user_login(self,driver):
        driver.find_element_by_xpath('//*[@id="user"]').clear()
        driver.find_element_by_xpath('//*[@id="user"]').send_keys('admin')
        driver.find_element_by_xpath('//*[@id="password"]').clear()
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="submit"]').click()

    #退出
    def user_logout(self,driver):
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/a[1]').click()
        time.sleep(10)
        driver.quit()
