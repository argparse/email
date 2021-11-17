#-*- coding: utf-8 -*-
from email.mime.text import MIMEText
import time
#timestr=time.strftime('%Y-%m-%d %X', time.localtime( time.time() ) )
#msg = MIMEText('hello, Nice to meet you send by Python...\n'+timestr, 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')
# 输入收件人地址:
to_addr = input('To: ')


import smtplib
import time
server = smtplib.SMTP(smtp_server,25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
for i in range(100):
    time.sleep(1)
    timestr=time.strftime('%Y-%m-%d %X', time.localtime( time.time() ) )
    msg = MIMEText('你是一头250斤于彦猪\n'+timestr, 'plain', 'utf-8')
    server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()