# -*- coding: UTF-8 -*-
from selenium import webdriver
from public import Login

class LoginTest():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://xktj.gongf.com/login")
        self.driver.maximize_window()

    #admin用户登录
    def test_admin_login(self):
        username = 'admin'
        password = '123456'
        Login().user_login(self.driver,username,password)
        self.driver.quit()

    # king用户登录
    def test_king_login(self):
        username = 'king'
        password = '123123'
        Login().user_login(self.driver, username, password)
        self.driver.quit()



LoginTest().test_admin_login()
LoginTest().test_king_login()

