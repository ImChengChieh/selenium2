# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    '''百度搜索测试'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        '''搜索关键字:HTMLTestRunner'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
        # time.sleep(2)
        # title = driver.title
        # self.assertEqual(title, "unittest-百度搜索")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":

    # testunit = unittest.TestSuite()
    # testunit.addTest(Baidu("test_baidu_search"))

    #按照一定格式获取当前时间
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # #定义报告存放路径
    # filename = './' + now +'result.html'
    #
    # fp = open(filename,'wb')
    # #定义测试报告
    # runner = HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行情况：')
    # runner.run(testunit)    #运行测试用例
    # fp.close()              #关闭报告文件
    unittest.main()