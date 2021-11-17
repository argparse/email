# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re

# a queue of urls to be crawled
new_urls = deque(['http://www.cdtf.gov.cn/cdtfxq/baohu/2021-02/26/content_1322a55ab6994b189067ab4c7d9a4014.shtml'])

# a set of urls that we have already crawled
processed_urls = set()

# a set of crawled emails
emails = set()
mail_list = []

try:
# process urls one by one until we exhaust the queue
 while len(new_urls):

    # move next url from the queue to the set of processed urls
    url = new_urls.popleft()
    processed_urls.add(url)

    # extract base url to resolve relative links
    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/') + 1] if '/' in parts.path else url

    # get url's content
    print("Processing %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        # ignore pages with errors
        continue

    # extract all email addresses and add them into the resulting set
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    for val in list(new_emails):
        #if '.png' or '.jpg' or '.js' or '.jpeg' in val:
        if '.jpg' in val:

            new_emails.remove(val)
        elif '.png' in val:

            new_emails.remove(val)
        elif '.jpeg' in val:

            new_emails.remove(val)
        elif '.css' in val:

            new_emails.remove(val)
        elif '.js' in val:

            new_emails.remove(val)

    emails.update(new_emails)

    # create a beutiful soup for the html document
    soup = BeautifulSoup(response.text, "html.parser")

    # find and process all the anchors in the document
    for anchor in soup.find_all("a"):
        # extract link url from the anchor
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        # resolve relative links
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link
        # add the new url to the queue if it was not enqueued nor processed yet
        if not link in new_urls and not link in processed_urls:
            new_urls.append(link)
    print(','.join(emails))
    mail_list.append(','.join(emails))
    if len(mail_list)>500:
        mail_list = list(filter(None, mail_list))
        break
except Exception as e:
    pass




'''
for i in range(0, 10000):
    #print(i)
    a = ("%s@163.com" % i)
    mail_list.append(a)'''



smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'lan.zi.jian.nankai@gmail.com'
password = 'whoamI404'
sender = 'lan.zi.jian.nankai@gmail.com'
targets = mail_list
msg = MIMEMultipart()
msg['Subject'] = """尊敬的领导您好，我们反应现成都市双流区局级公务员，兰子鉴，（原绵阳市小枧镇党委副书记），涉黑，持械伤人，有案底"""
msg['From'] = sender
msg['To'] = ', '.join(targets)
print(msg['To'])

txt = MIMEText("""尊敬的领导您好，我们反应现天府新区生态环境和城市管理局副局长，兰子鉴，（原绵阳市小枧镇党委副书记），涉黑，持械伤人，有案底, 自媒体之前已有报道:
https://chengdugov.wordpress.com/
 http://scientificresearch.website/lanzijian/
 https://argparse.github.io/


兰子鉴曾在打麻将输钱后持械把受害者打成颅骨骨折，见附件图片.


涉黑村霸兰子鉴: 
身份证:510722198809100018   [籍贯四川省绵阳市三台县(男, 属龙,处女座)] 

QQ号: 673578531

微信号: lan673578531

✉️邮箱:jackiemind@163.com

固定电话:0816-2382593


兰子鉴靠行贿领导，一年内连升三级，现在已经从绵阳市小枧镇党委副书记摇身一变变成了局级干部



希望有关部门领导严惩凶手！



此致



敬礼





兰子鉴持械伤人案受害者亲属





"""
)
msg.attach(txt)

filepath = 'C:\\Users\\williamyangy\\Bill\\revenge\\Capture.jpg'
with open(filepath, 'rb') as f:
    img = MIMEImage(f.read())

img.add_header('Content-Disposition',
               'attachment',
               filename=os.path.basename(filepath))
msg.attach(img)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)

server.sendmail(sender, targets, msg.as_string())
server.quit()
