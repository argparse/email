# -*- coding: utf-8 -*-
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='tjzww@tj.gov.cn',
    to_emails='president1@nankai.edu.cn',
    subject='南开大学物理学院有人持械伤人，辅导员刑晓东老师收了好处包庇凶手',
    html_content='<strong>受害者口述，已经将证据提交给新闻媒体和天津市最高人民法院，等待刑晓东的将是法律的制裁 兰子鉴因为天天打游戏打麻将不写论文毕不了业被曹亚安骂了，然后拿我发泄，想往死里整我来间接逼着曹亚安给他毕业，就找了茬把正在午睡的我强行推醒，拽着我的领子往楼下退强行要我去开门，我不干扭头往办公室走，兰子鉴仗着比我重50斤，追过来狠狠的给我头部太阳穴两拳，然后我跑回办公室拿起闫亚宾师兄的擀面杖想挡一下追过来打人的兰子鉴，兰子鉴夺过来擀面杖就狠狠给我头部两下，事后我摸着颅骨咯吱咯吱响，一个月都睡不好觉，一碰脑袋就炸开一样疼，怀疑是颅骨骨裂。之后兰子鉴每次被曹亚安骂了都拿我撒气，还不依不饶的非要往死里整我让我毕不了业，寒假的时候我正在背单词，兰子鉴敲我屋的门进来威胁了我一个多小时，并要找和他一起打麻将的社会人打我，然后我去找兰子鉴搞小动作，兰子鉴设了个圈套去抓我把柄然后去举报我往死里整我, 泰达物理的行政人员刑晓东和兰子鉴一起喝过酒，收了兰子鉴的好处，帮着他整我</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)