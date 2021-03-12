# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 下午 03:48
# @Author  : super man
# @FileName: send_email.py
# @Software: PyCharm

"""
E_mail.py 配置收发邮件
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import sys
import io
import os
import time


def send_email():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

    smtpserver = 'smtp.qq.com'  # 发件服务器
    port = 465  # 端口    服务器和端口号不知道的话，可以去qq邮箱搜索
    username = '1547066086@qq.com'  # 发件箱用户名
    password = 'bbxlbbgpwcpbfhgc'  # 授权码，注意这里不是密码，是qq邮箱支持第三方工具的授权码，需要去qq邮箱修改
    sender = '1547066086@qq.com'  # 发件人邮箱
    receiver = '2695850180@qq.com'  # 收件人邮箱
    # receiver = ['2695850180@qq.com']  # 多个收件人写成列表就可以了

    msg = MIMEMultipart('related')  # 定义邮件类型，related可以增加多种附件
    msg.attach(MIMEText('本轮自动化测试报告已发送，望领导查阅'))  # 邮件里边的文本
    msg['From'] = sender  # 让发件人不为空
    msg["Subject"] = Header("自动化测试报告", "utf-8").encode()
    msg["To"] = Header("测试负责人 <%s>" % receiver)
    msg["date"] = time.strftime("%a,%d %b %Y %H:%M:%S %z")

    # 下边这几句是添加附件
    pwd = os.getcwd()  # 获取当前目录路径
    pwd_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")  # 获取当前目录父目录路径
    index_path = os.path.join(pwd_father, 'report.html')  # 测试报告目录路径
    print(index_path)
    mail_path = open(index_path, 'r', encoding='utf-8').read()  # 这几句里边可以修改路径和文件名称，具体以实际为准
    att = MIMEText(mail_path, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = 'index.html'"
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)  # 连接邮件服务器
    smtp.login(username, password)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送，接收，内容
    smtp.quit()  # 关闭
    print("邮件发送成功")  # 提示邮件发送结果
