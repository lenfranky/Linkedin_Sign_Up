#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'LZ'

import time
import requests
import re

"""
利用yima平台的API获得手机号及验证码等操作
"""
class Phone(object):
    def __init__(self, username=' ', password=' '):
        self.token = self.get_token(username, password)

    """
    向API发送请求，并打印接收的数据
    """
    def get_value(self, url):
        headers = {}
        params = {}
        req = requests.get(self, url, headers=headers, params=params)
        print(req.text)
        return req

    """
    得到账号所对应的token
    """
    def get_token(self, username=' ', password=' '):
        headers = {}
        params = {}
        url = "http://api.fxhyd.cn/UserInterface.aspx?action=login&username=%s&password=%s" % (username, password)
        req = requests.get(url, headers=headers, params=params)
        token = req.text.split('|')[1]
        print "the token is:\t" + str(token)
        return token

    """
    得到手机号
    """
    def get_phone_num(self):
        url_get_phonenumber = "http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token=%s&itemid=2656" % self.token
        headers = {}
        params = {}
        req = requests.get(url_get_phonenumber, headers=headers, params=params)
        phone_number = req.text.split('|')[1]
        print "the phone_number is:\t" + str(phone_number)
        return phone_number

    """
    获取短信
    """
    def get_message(self, phone_number):
        url_get_message = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=%s&itemid=2656&mobile=%s" % (
        self.token, phone_number)
        headers = {}
        params = {}
        wait_time = 60*2
        req = requests.get(url_get_message, headers=headers, params=params)
        word_has_succesed = req.text.split('|')[0]
        # print "the message is:\t" + str(req.text)
        time_start = time.time()
        time_now = time.time()
        while (time_now - time_start) < wait_time and not word_has_succesed == "success":
            req = requests.get(url_get_message, headers=headers, params=params)
            word_has_succesed = req.text.split('|')[0]
            time_now = time.time()
            time.sleep(1)

        if word_has_succesed == "success":
            text = req.text.split('|')[1]
            time_waited = time_now - time_start
            print '短信内容是:\t' + str(text) + '\n接收验证码短信耗费时长:\t' + str(time_waited) + 's'
            return text
        else:
            print "未收到短信!"

    """
    从短信中获得验证码
    """
    def get_verification_code(self, text):
        pat = "[0-9]+"
        IC = 0
        IC = re.search(pat, text)
        v_code = IC.group()
        if IC:
            print"验证码是:\t" + str(v_code)
        else:
            print"请重新设置表达式"
        return v_code

    """
    手机号使用之后进行释放
    """
    def release_phone_num(self, phone_num):
        url_release = 'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=%s&itemid=2656&mobile=%s' % (
        self.token, phone_num)
        headers = {}
        params = {}
        req = requests.get(url_release, headers=headers, params=params)
        #print req.text
        #print type(phone_num)
        if req.text == "success":
            print "手机号码成功释放:\t%s" %(str(phone_num))


"""
if __name__ == '__main__':

    url = "http://api.fxhyd.cn/UserInterface.aspx?action=login&username= &password= "
    url_get_phonenumber = "http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token=005112943a6dc1f02b0a7e63fdcdc9bc0257bdff&itemid=2656"


    # baidu_func(url)
    list = get_value(url_get_phonenumber)
    # list = str(list.text)
    # print list
    list = list.text.split('|')[1]
    print list
    # baidu_func(url_3)
    url_get_message = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=TOKEN&itemid=2656&mobile=%s"%list
    get_value(url_get_message)
"""
"""
if __name__ == '__main__':
    phone = Phone(username=' ', password=' ')
    #token = phone.get_token(username=' ', password=' ')
    phone_number = phone.get_phone_num()
    text_message = phone.get_message(phone_number)
    if text_message:
        code = phone.get_verification_code(text_message)
"""

if __name__ == '__main__':
    phone = Phone(username=' ', password=' ')
    text_message = phone.get_message('15584341678')
    if text_message:
        code = phone.get_verification_code(text_message)
    phone.release_phone_num('15584341678')