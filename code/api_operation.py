# -*- coding:utf-8 -*-
__author__ = 'LZ'

import code.Phone_api

"""
用于手动操作释放手机号等操作
"""
if __name__ == '__main__':
    phoneObj = code.Phone_api.Phone()
    phone_num = phoneObj.get_phone_num()
    print phone_num
    phoneObj.release_phone_num(phone_num)