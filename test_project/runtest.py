# -*- coding: UTF-8 -*-
# import unittest,time
# from HTMLTestRunner import HTMLTestRunner
#
#
# # 为了解决添加用例的问题
# # 定义测试用例的目录为当前目录
# test_dir = './test_case'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
#
# if __name__ == '__main__':
#     # runner = unittest.TextTestRunner()
#     # runner.run(discover)
#
#     # 按照一定格式获取当前时间
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     #定义报告存放路径
#     filename = 'report/' + now +'result.html'
#
#     fp = open(filename,'wb')
#     #定义测试报告
#     runner = HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
#     runner.run(discover)    #运行测试用例
#     fp.close()              #关闭报告文件

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib,unittest,time,os

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#定义邮件发送
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    smtp = smtplib.SMTP_SSL()
    smtp.connect("smtp.qq.com")
    smtp.login("2476159529@qq.com","dmsymqizlgsqdhjb")
    smtp.sendmail("2476159529@qq.com",['a13056432125@163.com','595887491@qq.com'],msg.as_string())
    smtp.quit()
    print ('邮箱发送成功！')

#=======查找测试报告目录，找到最新生成的测试报告文件=======
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + "\\" +fn))
    file_new = os.path.join(testreport,lists[-1])
    print (file_new)
    return file_new

if __name__ == '__main__':
    test_dir = 'F:\\Selenium\\test_project\\test_case'
    test_report = 'F:\\Selenium\\test_project\\report'

    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = 'report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report) #发送测试报告


