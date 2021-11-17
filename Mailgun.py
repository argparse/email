# -*- coding: utf-8 -*-
import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxc962207faa12427092f5468d5d0dde02.mailgun.org/messages",
		auth=("api", "0bf928df8e60b05f3c84d7c61b83116c-360a0b2c-e59f8ebd"),
		data={"from": "天津政务<tjzww@tj.gov.cn>",
			"to": "jwjcs@nankai.edu.cn<jwjcs@nankai.edu.cn>",
			"subject": "南开大学物理学院刑晓东老师组织公款吃喝一事，已经被举报到天津市纪委",
			"text": "南开大学物理学院刑晓东老师组织公款吃喝一事，已经被举报到天津市纪委，纪委巡视组将会在下个月组织对南开大学物理学院刑晓东老师公款吃喝的调查"})

send_simple_message()