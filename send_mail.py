# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText                #用于定义邮件正文      email模块
from email.header import Header                     #用于定于邮件标题
from email.mime.multipart import MIMEMultipart      #通过MIMEMultipart()模块构造的带附件的邮件

#发送邮箱服务器
smtpbserver = 'smtp.qq.com'
#发送邮箱用户/密码
user = '2476159529@qq.com'
password = 'dmsymqizlgsqdhjb'
#发送邮箱
sender = '2476159529@qq.com'
#接收邮箱
# receiver = ['595887491@qq.com','a13056432125@163.com']      #由于可以一次发给多个人，所以传入一个list
receiver = ['a13056432125@163.com']
#发送邮箱主题
subject = 'Python email test'
#编写HTML类型的邮件正文
# msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
# msg['Subject'] = Header(subject,'utf-8')
#发送的附件
sendfile = open('F:\\Selenium\\test_project\\report.txt','rb').read()

att = MIMEText(sendfile,'base64','utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename="report.txt"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

#连接发送邮件
# smtp = smtplib.SMTP()
smtp = smtplib.SMTP_SSL()
# smtplib.SMTPAuthenticationError: (530, 'Error: A secure connection is requiered(such as ssl).
smtp.connect(smtpbserver)
smtp.set_debuglevel(1)                  #打印出和SMTP服务器交互的所有信息
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()
