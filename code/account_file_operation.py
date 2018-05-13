# -*-coding:utf-8 -*-
__author__ = 'LZ'

import codecs

"""
用于实现对记录邮箱账号的txt文档的操作
"""
class file_mailbox_account(object):
    """
    从文档中读取账户数据
    """
    def read_account(self,path = r'../data/mailbox_account.txt'):
        file = codecs.open(path, mode = 'r', encoding='utf-8')
        line_num = 0
        flag_find_line = False
        for line in file:
            #line.replace('\n','')
            line_text = line.strip()
            word_list = line_text.split(' ')
            #word_list[2] = word_list[2].split()[0]
            flag_has_processed = word_list[2]
            if flag_has_processed == '0':
                print "从txt文档中读取的行：\t" + str(line_num)
                flag_find_line = True
                break
            else:
                line_num += 1

        if flag_find_line:
            self.new_line_id = line_num

            file.close()
            return word_list, line_num
        else:
            print "文件中所有行邮箱账号都已被注册！"
            file.close()
            return None

    """
    对于邮箱账户文件重写
    :param path :   邮箱账户文件的位置
    :param line_id_processed    ;   已经处理过的账户的行数(从零开始）
    """
    def write_account(self,path = r'../data/mailbox_account.txt',line_id_processed = -1):
        file_read = codecs.open(path, mode='r', encoding='utf-8')
        new_file_data = ""
        line_num = 0
        for line in file_read:
            # print line
            # 删掉每行末尾的换行符
            new_line = line.replace('\r\n', '')
            new_line = new_line.split(' ')
            new_line = new_line[0:2]
            new_line = ' '.join(new_line)
            # print new_line
            new_file_data += new_line

            if line_num > line_id_processed:
                new_file_data += ' 0\n'
            else:
                new_file_data += ' 1\n'

            line_num += 1
        file_read.close()

        # path = "mailbox_account.txt"
        path_write = path
        file_out = codecs.open(path_write, mode='w', encoding='utf-8')
        file_out.write(new_file_data)
        file_out.close()
        print "txt文档中第%d行数据已成功写入" %line_id_processed

if __name__ == '__main__':
    file = file_mailbox_account()
    # line_id_processed == 99时则可以使得文档中所有账号均被标注为"1"
    file.write_account(path=r'../data/mailbox_account.txt', line_id_processed=-1)
    list = file.read_account(path=r'../data/mailbox_account.txt')
    if list:
        print list