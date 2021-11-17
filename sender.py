# -*- coding: utf-8 -*-
import os
import smtplib

from email.mime.text import MIMEText

from email.utils import formataddr

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# from email.mime.application import MIMEApplication

my_sender = 'lan.zi.jian.nankai@gmail.com'  # 发件人邮箱账号

my_pass = 'whoamI404'
#luping@nankai.edu.cn, nknews@nankai.edu.cn, xxbxxb@nankai.edu.cn, nk610@nankai.edu.cn, tyb@nankai.edu.cn, rsc@nankai.edu.cn, search@index.result, ennews@nankai.edu.cn, shnankai@vip.163.com, chaxin@nankai.edu.cn, liuyan@nankai.edu.cn, prbrgrace@yahoo.com, tsg@nankai.edu.cn, President01@nankai.edu.cn, nklwhtg@163.com, zhshb@nankai.edu.cn, service@wanfangdata.com.cn, XXGK@NANKAI.EDU.CN, nkuaa@nankai.edu.cn, ref@nankai.edu.cn, marketing3@emeraldinsight.com.cn, jjjc@nankai.edu.cn, jo.smith@university.ac.uk, nankaiboshibiye@sohu.com, nkjjh@nankai.edu.cn, xxgk@nankai.edu.cn, hyzsb@nankai.edu.cn, President02@nankai.edu.cn, acs-logo@2x.png, nyma998@gmail.com, nkuniversity@nankai.edu.cn, yangyidong@nankai.edu.cn, acq@nankai.edu.cn, xgbjyxck@nankai.edu.cn, zzb507@nankai.edu.cn, lisy@nankai.edu.cn, zlfzb@nankai.edu.cn, President03@nankai.edu.cn, ill@nankai.edu.cn, xxjd@nankai.edu.cn
my_user = 'xuwq@jlu.edu.cn'  # 收件人邮箱账号，我这边发送给自己

mail_msg = """

已经将证据提交给新闻媒体和天津市最高人民法院，等待刑晓东的将是法律的制裁, 受害者口述，:'
兰子鉴因为天天打游戏打麻将不写论文毕不了业被曹亚安骂了，然后拿我发泄，想往死里整我来间接逼着曹亚安给他毕业，就找了茬把正在午睡的我强行推醒，拽着我的领子往楼下退强行要我去开门，我不干扭头往办公室走，兰子鉴仗着比我重50斤，追过来狠狠的给我头部太阳穴两拳，然后我跑回办公室拿起闫亚宾师兄的擀面杖想挡一下追过来打人的兰子鉴，兰子鉴夺过来擀面杖就狠狠给我头部两下，事后我摸着颅骨咯吱咯吱响，一个月都睡不好觉，一碰脑袋就炸开一样疼，怀疑是颅骨骨裂。
之后兰子鉴每次被曹亚安骂了都拿我撒气，还不依不饶的非要往死里整我让我毕不了业，寒假的时候我正在背单词，兰子鉴敲我屋的门进来威胁了我一个多小时，并要找和他一起打麻将的社会人打我，然后我去找兰子鉴搞小动作，兰子鉴设了个圈套去抓我把柄然后去举报我往死里整我, 泰达物理的行政人员刑晓东和兰子鉴一起喝过酒，收了兰子鉴的好处，帮着他整我'




<p><a href="https://argparse.github.io">证据资料，请点击这个链接</a></p>

<p><b><a href="https://argparse.github.io">收受贿赂包庇凶手的南开大学物理学院辅导员刑晓东资料 : 电子邮箱： xingxd@nankai.edu.cn 身份证号: 120104197812147615  </a><b></p>
"""

'''def mail():
    ret = True

    try:

        msg = MIMEText(mail_msg, 'html', 'utf-8')  # 'plain'为文本,'html为网页

        msg['From'] = formataddr(["淮阴工学院女生ppq", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号

        # msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        msg['To'] = my_user

        msg['Subject'] = "淮阴工学院数理学部青年教师于彦龙, 性侵女学生, 脚踏两只船"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25

        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

        server.sendmail(my_sender, my_user.split(','), msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件

        server.quit()  # 关闭连接

    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False

        ret = False

    return ret


ret = mail()

if ret:

    print("邮件发送成功")

else:

    print("邮件发送失败")'''

#attachment

def mail():
    ret = True

    try:

        msg = MIMEMultipart()
        msg.attach(MIMEText(mail_msg, 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的png文件
        img_data = open('兰子鉴持械伤人_受害者在医院抢救.mp4', 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename('兰子鉴持械伤人_受害者在医院抢救.mp4'))
        msg.attach(image)

        msg['From'] = formataddr(["yy", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号

        # msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        msg['To'] = my_user

        msg['Subject'] = "南开大学物理学院有人持械伤人，辅导员刑晓东老师收了好处包庇凶手"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25

        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码


        server.sendmail(my_sender, my_user.split(','), msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件

        server.quit()  # 关闭连接

    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False

        ret = False

    return ret


ret = mail()

if ret:

    print("邮件发送成功")

else:

    print("邮件发送失败")


