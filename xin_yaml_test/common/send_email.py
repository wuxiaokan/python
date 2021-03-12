# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 下午 03:48
# @Author  : super man
# @FileName: send_email.py
# @Software: PyCharm

"""
E_mail.py 配置收发邮件
"""
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import os


def send_mail(new_report):
    f = open(new_report, "rb")
    mail_body = f.read()
    f.close()

    username = "1547066086@qq.com"  # 发件箱用户名
    password = "bbxlbbgpwcpbfhgc"  # 发件箱密码（授权码）
    sender = "1547066086@qq.com"  # 发件人邮箱
    receiver = ["2695850180@qq.com"]  # 收件人邮箱
    # 邮件正文是MIMEText
    msg = MIMEText(mail_body, "html", "utf-8")

    # 邮件对象
    msg["Subject"] = Header("自动化测试报告", "utf-8").encode()
    msg["From"] = Header(u"测试机 <%s>" % sender)
    msg["To"] = Header("测试负责人 <%s>" % receiver)
    msg["date"] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")  # 邮箱服务器
    smtp.login(username, password)  # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    return file_new
