# -*- coding: UTF-8 -*-
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# # 第三方 SMTP 服务
# mail_host = "smtp.163.com"  # 设置服务器
# mail_user = "a13056432125@163.com"  # 用户名
# mail_pass = "a13056432125"  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格
#
# sender = 'a13056432125@163.com'
# receivers = 'c13056432125@163.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# message = MIMEText('a test for python', 'plain', 'utf-8')
# # message['From'] = Header("ppyy", 'utf-8')
# # message['To'] = Header("you", 'utf-8')
#
# subject = 'my test'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP_SSL(mail_host, 465)
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     smtpObj.quit()
#     print u"邮件发送成功"
# except smtplib.SMTPException, e:
#     print e

import smtplib
from email.mime.text import MIMEText


def send_email(host, username, passwd, send_to, subject, content):
    msg = MIMEText(content.encode('utf8'), _subtype='html', _charset='utf8')
    msg['From'] = username
    msg['Subject'] = u'%s' % subject
    msg['To'] = ",".join(send_to)

    try:
        s = smtplib.SMTP_SSL(host, 465)
        s.login(username, passwd)
        s.sendmail(username, send_to, msg.as_string())
        s.close()
    except Exception as e:
        print 'Exception: send email failed', e


if __name__ == '__main__':
    host = 'smtp.qq.com'
    username = '2476159529@qq.com'
    passwd = 'dmsymqizlgsqdhjb'
    to_list = ['a13056432125@163.com', '1071017575@qq.com']
    subject = u"邮件主题"
    content = u'使用Python发送邮件'
    send_email(host, username, passwd, to_list, subject, content)