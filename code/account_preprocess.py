# -*-coding:utf-8 -*-
__author__ = 'LZ'

import codecs

def account_preprocess(path_read=r'../data/mailbox_account_origin.txt', path_write=r'../data/mailbox_account.txt'):
    #读取初始文件
    #path = 'mailbox_account_origin.txt'
    file_read = codecs.open(path_read, mode='r', encoding='utf-8')
    new_file_data = ""
    for line in file_read:
        #print line
        #删掉每行末尾的换行符
        new_line = line.replace('\r\n', '')
        new_line = new_line.split('----')
        new_line = ' '.join(new_line)
        """
        for word in line:
            if word == '\n' or word == '\r':
                continue
            new_line += word
            print new_line
        """
        #print new_line
        new_file_data += new_line
        new_file_data += ' 0\n'
    file_read.close()

    #path = "mailbox_account.txt"
    file_out = codecs.open(path_write, mode='w', encoding='utf-8')
    file_out.write(new_file_data)
    file_out.close()

if __name__ == "__main__":
    path_origin = r'../data/mailbox_account_origin.txt'
    path_processed = r'../data/mailbox_account.txt'
    account_preprocess(path_read=path_origin, path_write=path_processed)