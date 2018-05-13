# -*- coding:utf-8 -*-
__author__ = 'LZ'

import code.linkedin_operation

if __name__ == '__main__':
    user = 'fzdwxxcl' #使用者的姓名缩写，为了写入excel文档中

    username = ' '
    password = ' '

    code.linkedin_operation.complete_process(user, username, password)
