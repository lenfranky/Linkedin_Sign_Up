#!/usr/bin/python
# -*-coding:utf-8 -*-
__author__ = 'LZ'

import os
import win32com.client
import sys
import time
import setname
import socket
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

"""
用于实现储存已经注册过的账户信息的excel文档的相关操作
"""
class ExcelOperation(object):
    def __init__(self,path_excel=r'../data/excel_file.xls'):
        self.path = self.get_path_abs(path_relative=path_excel)
        #self.path = r'C:\Users\32779\OneDrive\codes\learning\data\excel_file.xls'
        #self.new_line_id = self.get_new_line_id(self.path)
        #print self.new_line_id

        self.get_data(user='lz', account='fzdwxxcl@sina.com', password='fzdwxxcl314')

    """
    实现相对路径与绝对路径的转换
    """
    def get_path_abs(self, path_relative = r'../file_IO/excel_file.xls'):
        path_abs = os.path.abspath(path_relative)
        return path_abs

    """
    遍历excel文档，得到应该写入的行所在的位置
    """
    def get_new_line_id(self, path=r''):
        time.sleep(1)
        xlApp = win32com.client.Dispatch('Excel.Application')  # 打开EXCEL，这里不需改动
        myexcel = xlApp.Workbooks.Open(path)  # 将D:\\1.xls改为要处理的excel文件路径
        excel_sheet = myexcel.Worksheets(1)

        line_id = 1
        find_line_flag = False
        # 读取出的None为instance类型，而不是NoneType类型
        str_None = 'None'

        while not find_line_flag:
            line_first_value = excel_sheet.Cells(line_id, 1)
            # print type(line_first_value)
            str_temp = str(line_first_value)
            if str_temp == str_None:
                # print line_first_value
                find_line_flag = True
            else:
                line_id += 1

        myexcel.Close(SaveChanges=1)  # 完成 关闭保存文件
        xlApp.Quit()

        self.new_line_id = line_id
        print "目前excel中共有%d行数据" % (line_id - 1)
        return line_id

    """
    将信息整合到列表中，等待之后的写入操作
    """
    def get_data(self, user='fzdwxxcl', account='fzdwxxcl@sina.com', password='fzdwxxcl314', real_name=u'复杂多维信息处理'):
        # 获取本机电脑名
        PC_name = socket.getfqdn(socket.gethostname())
        # 获取本机ip
        PC_IP = socket.gethostbyname(PC_name)
        self.IP = PC_IP

        account_mailbox = account
        password_mailbox = password
        account_linkedin = account
        password_linkedin = password
        realName_linkedin = real_name
        foreignName_linkedin = 'fzdwxxcl'
        country_province = u'中国四川成都'
        is_student = '1'
        position = ''
        company_name = ''
        school_name = u'四川大学'
        is_mailbox = '1'
        person_registered = user
        IP_address = u'125.71.229.23'

        self.value_row = [account_mailbox, password_mailbox, account_linkedin, password_linkedin, realName_linkedin, \
                     foreignName_linkedin, country_province, is_student, position, company_name, school_name, \
                     is_mailbox, person_registered, IP_address]
        #print self.value_row

    """
    注册完成之后在excel文档中储存信息
    """
    def write_new_line(self):
        time.sleep(1)
        new_line_id = self.get_new_line_id(self.path)
        # 打开EXCEL
        xlApp = win32com.client.Dispatch('Excel.Application')
        #此处应为excel文件的绝对路径
        myexcel = xlApp.Workbooks.Open(self.path)
        excel_sheet = myexcel.Worksheets(1)
        print "要向excel中写入的数据:\t" + str(self.value_row)
        excel_sheet.Range(excel_sheet.Cells(new_line_id, 1), excel_sheet.Cells(new_line_id, 14)).Value = self.value_row

        myexcel.Save()
        myexcel.Close()  # 完成 关闭保存文件
        xlApp.Quit()

        print "excel文件数据写入成功"

    def test(self):
        path_name_file = r'../data/name.txt'
        nameObj = setname.SetName(path_name_file=path_name_file)
        name = nameObj.get_name()
        print name
        # print unicode(name, 'utf-8')
        # u_name = u'%s'%name
        u_name = name.decode('utf-8')
        print u_name
        self.get_data(real_name=u_name)
        self.write_new_line()

if __name__ == '__main__':
    excel = ExcelOperation()
    #excel.get_data()
    #excel.write_new_line()
    excel.test()