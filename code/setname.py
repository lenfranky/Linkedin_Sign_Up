# coding:utf-8
__author__ = 'LZ'

import random
import codecs

class SetName():
    def __init__(self,path_name_file = r'../data/name.txt'):
        self.family_name = []
        self.given_name_male = []
        self.given_name_female = []
        self.get_data(path_name = path_name_file)

    def get_data(self,path_name = r'../data/name.txt'):
        file = codecs.open(path_name, mode='r', encoding="utf-8")
        num = 0
        for line in file:
            num += 1
            for word in line:
                if (word != '\n') and (word != ' ')and (word != '\r'):
                    #num += 1
                    if num == 2:
                        self.family_name.append(word)
                    elif num == 4:
                        self.given_name_male.append(word)
                    elif num ==6:
                        self.given_name_female.append(word)
        file.close()
    def get_name_not_common(self):
        # 得到一个1-10的随机整数
        # 若为1-10，则得到一个女生的名字，若为11-20，则得到一个男生的名字
        num = random.randint(1, 20)
        if num <= 10:
            if num <= 3:
                name = random.choice(self.family_name) + random.choice(self.given_name_female)
            else:
                name = random.choice(self.family_name) + random.choice(self.given_name_female) + random.choice(self.given_name_female)
        else:
            if num <= 13:
                name = random.choice(self.family_name) + random.choice(self.given_name_male)
            else:
                name = random.choice(self.family_name) + random.choice(self.given_name_male) + random.choice(self.given_name_male)
        return name

    def get_name_in_common(self):
        famaily_name = ['张', '金', '李', '王', '赵', '孙', '钱', '李', '周', '吴', '郑', '王', '冯', '陈']
        given_name_1 = ['玉', '明', '龙', '芳', '军', '玲', '康', '余', '元']
        given_name_2 = ['', '立', '玲', '', '国', '萌', '凝', '文', '展', '露', '静', '智', '丹', '宁', '', '', '']

        for iter in range(15):
            name = random.choice(famaily_name) + random.choice(given_name_1) + random.choice(given_name_2)
            #print(name)
        return name

    def get_name(self):
        num = random.randint(1,10)
        if num <= 7:
            name = self.get_name_in_common()
        else:
            name = self.get_name_not_common()
        return name

    def show(self):
        rand_family_name = random.choice(self.given_name_female)
        return rand_family_name



if __name__ == "__main__":
    setname = SetName(path_name_file = r'../data/name.txt')
    for iter in range(1000):
        print setname.get_name()