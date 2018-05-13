# -*- coding:utf-8 -*-
__author__ = 'LZ'

import code.setname
import code.Phone_api
import code.mailbox_operation
import code.account_file_operation
import code.excel_operation
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import sys

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')


class Linkedin_operation(object):
    def __init__(self, user='fzdwxxcl',username=' ', password=' '):
        self.user = user
        self.account = ''
        self.password = ''
        self.name = ''
        # self.phone_number = 0
        self.get_name()

        # txt_line用于储存目前正在处理的是txt文档中的第几行账户
        self.txt_line = 0
        # 打开txt文件并读入数据
        self.get_account()
        # account_txt_path用于储存账户所在的txt文档的位置
        self.account_txt_path = r'../data/mailbox_account.txt'
        # path_excel用于储存excel文件的位置
        path_excel = r'../data/excel_file.xls'
        self.phoneObj = code.Phone_api.Phone(username=username, password=password)
        self.phone_number = self.phoneObj.get_phone_num()
        self.driver = webdriver.Chrome()

    """
    从txt文件中得到文档的信息
    """
    def get_account(self):
        account_file = code.account_file_operation.file_mailbox_account()
        account_data, self.txt_line = account_file.read_account()
        self.account = account_data[0]
        self.password = account_data[1]
        # self.password = str(self.password).decode('utf-8')
        # print type(self.password)
        print "所使用的邮箱为:\t" + str(self.account)

    # 得到手机号码
    def get_phone_number(self):
        phone_num = self.phoneObj.get_phone_num()
        # self.phone_number = phone_num
        return phone_num

    # 得到验证码
    def get_v_code(self):
        text = self.phoneObj.get_message(self.phone_number)
        if text:
            v_code = self.phoneObj.get_verification_code(text)
            self.phoneObj.release_phone_num(self.phone_number)
        else:
            pass
        return v_code

    """
    得到一个随机的名字
    """
    def get_name(self):
        path_name_file = r'../data/name.txt'
        nameObj = code.setname.SetName(path_name_file=path_name_file)
        name = nameObj.get_name()
        u_name = name.decode('utf-8')
        self.name = u_name
        print "本次申请所使用的生成的中文名字为:\t%s"%u_name

    """
    领英进行注册，得到使用手机号码的账号
    """
    def sign_up(self):
        # driver = webdriver.Chrome()
        driver = self.driver
        url_register = 'https://www.linkedin.com/start/join?trk=hb_join'
        driver.get(url_register)
        driver.implicitly_wait(60)

        driver.find_element_by_id('real-name').send_keys(self.name)
        driver.find_element_by_id('foreign-name').send_keys('fzdwxxcl')
        driver.find_element_by_id('join-email').send_keys(self.phone_number)
        driver.find_element_by_id('join-password').send_keys(self.password)

        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, 'fill-v2')))
        driver.find_element_by_class_name('fill-v2').click()

        v_code = self.get_v_code()
        # print v_code
        time.sleep(1)
        driver.find_element_by_id('phone-pin').send_keys(v_code)
        time.sleep(1)
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, '//*[@id="uno-reg-join"]/div/div/div[2]/div/form/fieldset/button')))
        driver.find_element_by_xpath('//*[@id="uno-reg-join"]/div/div/div[2]/div/form/fieldset/button').click()
        time.sleep(3)

        new_register_url = 'https://www.linkedin.com/onboarding/start/profile-location/new/'
        old_register_url = 'https://www.linkedin.com/start/edit-profile?trk=uno-reg-join-join-now'
        driver.get(old_register_url)

        current_url = driver.current_url
        if current_url == new_register_url:
            try:
                selection_province = Select(driver.find_element_by_id('ember1635'))
                selection_province.select_by_value("4")  # 选择四川
                time.sleep(1)
                selection_province = Select(driver.find_element_by_id('ember1638'))
                selection_province.select_by_value("urn:li:fs_city:(cn,4-2)")  # 选择成都
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="ember1622"]').click()
                time.sleep(3)
                # driver.find_element_by_xpath('//*[@id="ember2148"]"]').click()
                driver.find_element_by_id('ember2146').click()
                time.sleep(1)
                input_school = driver.find_element_by_id('typeahead-input-for-school-name')
                input_school.send_keys(u'四川大学')
                time.sleep(0.5)
                edu_start_year_input = Select(driver.find_element_by_id('onboarding-profile-edu-start-year'))
                edu_start_year_input.select_by_value("2017")
                time.sleep(0.5)
                edu_get_year = Select(driver.find_element_by_id('onboarding-profile-edu-end-year'))
                edu_get_year.select_by_value("2021")
                time.sleep(1)
                driver.find_element_by_id('ember2866').click()
                time.sleep(2)
                driver.find_element_by_id('ember3384').click()
                time.sleep(2)
                driver.find_element_by_id('ember3433').click()
                time.sleep(2)
            except:
                selection_province = Select(driver.find_element_by_id('ember1619'))
                selection_province.select_by_value("4")  # 选择四川
                time.sleep(1)
                selection_province = Select(driver.find_element_by_id('ember1622'))
                selection_province.select_by_value("urn:li:fs_city:(cn,4-2)")  # 选择成都
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="ember1569"]').click()
                time.sleep(3)
                # driver.find_element_by_xpath('//*[@id="ember2148"]"]').click()
                driver.find_element_by_id('ember2148').click()
                time.sleep(1)
                input_school = driver.find_element_by_id('typeahead-input-for-school-name')
                input_school.send_keys(u'四川大学')
                time.sleep(0.5)
                edu_start_year_input = Select(driver.find_element_by_id('onboarding-profile-edu-start-year'))
                edu_start_year_input.select_by_value("2017")
                time.sleep(0.5)
                edu_get_year = Select(driver.find_element_by_id('onboarding-profile-edu-end-year'))
                edu_get_year.select_by_value("2021")
                time.sleep(1)
                driver.find_element_by_id('ember2446').click()
                time.sleep(2)
                driver.find_element_by_id('ember3338').click()
                time.sleep(2)
                driver.find_element_by_id('ember3387').click()
                time.sleep(2)
        else:
            WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'provinceSelect')))
            selection_province = Select(driver.find_element_by_id('provinceSelect'))
            selection_province.select_by_value("4")  # 选择四川
            time.sleep(1)
            selection_province = Select(driver.find_element_by_id('citySelect'))
            selection_province.select_by_value("4-2.610083")  # 选择成都
            time.sleep(2)
            WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, 'save-profile')))
            driver.find_element_by_class_name('save-profile').click()
            # driver.find_element_by_id('student').click()

            WebDriverWait(driver, 30).until(
                ec.presence_of_element_located((
                    By.XPATH, \
                    '//*[@id="nux-basic-profile"]/div/div/div[2]/form/fieldset/div[1]/div[2]/ul/li[2]/fieldset/div/label[1]')))
            driver.find_element_by_xpath(
                '//*[@id="nux-basic-profile"]/div/div/div[2]/form/fieldset/div[1]/div[2]/ul/li[2]/fieldset/div/label[1]').click()

            WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'school')))
            input_school = driver.find_element_by_id('school')
            input_school.send_keys(u'四川大学')
            edu_start_year_input = Select(driver.find_element_by_id('school-start-year'))
            edu_start_year_input.select_by_value("2017")
            time.sleep(0.5)
            edu_get_year = Select(driver.find_element_by_id('school-end-year'))
            edu_get_year.select_by_value("2021")
            time.sleep(0.5)
            WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, 'save-profile')))
            driver.find_element_by_class_name('save-profile').click()
            time.sleep(2)

            flag_success_registered = False
            while not flag_success_registered:
                # 可能会随机地出现多次可跳过的页面
                try:
                    driver.find_element_by_class_name('btn-skip').click()
                except:
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id="get-the-app-form"]/fieldset/div[5]/ul/li[1]/input').click()
                    except:
                        pass
                """
                try:
                    driver.find_element_by_class_name('btn-skip').click()
                    #time.sleep(2)
                except:
                    pass

                try:
                    #driver.find_element_by_class_name('unstyled fodal-skip').click()
                    driver.find_element_by_xpath('//*[@id="get-the-app-form"]/fieldset/div[5]/ul/li[1]/input')
                    #time.sleep(2)
                except:
                    pass

                try:
                    driver.find_element_by_class_name('unstyled fodal-skip').click()
                    #time.sleep(2)
                except:
                    pass

                try:
                    driver.find_element_by_class_name('unstyled fodal-skip').click()
                    #time.sleep(2)
                except:
                    pass
                try:
                    driver.find_element_by_class_name('btn-skip').click()
                    #time.sleep(2)
                except:
                    pass
                """

                time.sleep(0.5)

                current_url = driver.current_url
                state_now = current_url.split('/')
                state_now = state_now[3]

                if state_now == 'in':
                    flag_success_registered = True

        # time.sleep(30000)
        # driver.close()

    """
    使用手机号的账户进行登陆
    """
    def log_in(self):
        self.driver.quit()
        self.driver = webdriver.Chrome()
        driver = self.driver
        url_log_in = 'https://www.linkedin.com/uas/login'
        driver.get(url_log_in)
        # driver.find_element_by_id('session_key-login').send_keys(self.phone_number)
        driver.find_element_by_id('session_key-login').send_keys(self.phone_number)
        driver.find_element_by_id('session_password-login').send_keys(self.password)
        driver.find_element_by_css_selector('input#btn-primary.btn-primary').click()
        time.sleep(3)

    """
    使用邮箱作为账户名进行登陆
    """
    def log_in_second(self):
        self.driver.quit()
        self.driver = webdriver.Chrome()
        driver = self.driver
        """
        all_handles = driver.window_handles
        for handle in all_handles:
            driver.switch_to_window(handle)
            driver.close()
        """

        url_log_in = 'https://www.linkedin.com/uas/login'
        driver.get(url_log_in)
        # driver.find_element_by_id('session_key-login').send_keys(self.phone_number)
        driver.find_element_by_id('session_key-login').send_keys(self.account)
        driver.find_element_by_id('session_password-login').send_keys(self.password)
        driver.find_element_by_css_selector('input#btn-primary.btn-primary').click()
        time.sleep(3)

    """
    在账户的设置界面添加邮箱账号
    """
    def add_mail_box(self):
        driver = self.driver
        # 打开“我的”下拉菜单
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, 'nav-item__title-container')))
        # time.sleep(3)
        # driver.find_element_by_xpath('//*[@id="nav-settings__dropdown-trigger"]/div/span[2]/li-icon/svg').click()
        driver.find_element_by_class_name('nav-item__title-container').click()
        time.sleep(1)
        # driver.find_element_by_class_name('nav-dropdown__item nav-settings__dropdown-item Sans-14px-black-60%').click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="nav-settings__dropdown-options"]')))
        # print "found it!"
        # 选中“设置和隐私”
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.LINK_TEXT, u'设置和隐私')))
        driver.find_element_by_link_text(u'设置和隐私').click()
        # WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, '//*[@id="nav-settings__dropdown-options"]'))).find_element_by_xpath('//*[@id="ember2481"]').click()
        # driver.find_element_by_xpath('//*[@id="ember2481"]').click()
        time.sleep(1)

        # 将tab转换到下一个页面
        current_url = driver.current_url
        # print current_url
        all_handles = driver.window_handles
        # print all_handles
        current_handle = driver.current_window_handle

        handle_id = 0
        for handle in all_handles:
            if current_handle == handle:
                driver.switch_to_window(all_handles[handle_id + 1])
                break
            else:
                handle_id += 1

        current_url = driver.current_url
        # print current_url

        # 打开“邮箱地址”选栏
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, '//*[@id="setting-email"]/a')))
        driver.find_element_by_xpath('//*[@id="setting-email"]/a').click()
        time.sleep(1)
        driver.find_element_by_class_name('add-email-address').click()
        add_email_input = driver.find_element_by_id('add-email-address')
        add_email_input.send_keys(self.account)
        send_email_button = driver.find_element_by_class_name('send-verification')
        send_email_button.click()

        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'verify-password')))
        driver.find_element_by_id('verify-password').send_keys(self.password, Keys.ENTER)

        # WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, '//*[@id="setting-email-add"]/span/form/div/button')))
        # driver.find_element_by_xpath('//*[@id="setting-email-add"]/span/form/div/button').click()

    """
    在用户的设置界面删去所使用的手机号
    """
    def delete_phone_num(self):
        self.log_in_second()
        driver = self.driver

        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, 'nav-item__title-container')))
        # time.sleep(3)
        # driver.find_element_by_xpath('//*[@id="nav-settings__dropdown-trigger"]/div/span[2]/li-icon/svg').click()
        driver.find_element_by_class_name('nav-item__title-container').click()
        time.sleep(1)
        # driver.find_element_by_class_name('nav-dropdown__item nav-settings__dropdown-item Sans-14px-black-60%').click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="nav-settings__dropdown-options"]')))
        # print "found it!"
        # 选中“设置和隐私”
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.LINK_TEXT, u'设置和隐私')))
        driver.find_element_by_link_text(u'设置和隐私').click()
        time.sleep(1)
        current_url = driver.current_url
        # print current_url
        all_handles = driver.window_handles
        # print all_handles
        current_handle = driver.current_window_handle

        # 将页面切换至下一tab
        handle_id = 0
        for handle in all_handles:
            if current_handle == handle:
                driver.switch_to_window(all_handles[handle_id + 1])
                break
            else:
                handle_id += 1

        # 打开“联系电话”选栏
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, '//*[@id="setting-phone"]/a')))
        driver.find_element_by_xpath('//*[@id="setting-phone"]/a').click()
        # time.sleep(1)
        # 点击“删除”按钮
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="phone-"]/ul/li[2]/span[2]/button')))
        driver.find_element_by_xpath('//*[@id="phone-"]/ul/li[2]/span[2]/button').click()
        # 在文本框中输入密码
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'verify-password')))
        driver.find_element_by_id('verify-password').send_keys(self.password, Keys.ENTER)
        time.sleep(1)
        driver.quit()

    """
    注册完成之后进行数据的保存
    """
    def save_data(self):
        # txt文档操作
        account_file = code.account_file_operation.file_mailbox_account()
        account_file.write_account(path=self.account_txt_path, \
                                   line_id_processed=self.txt_line)

        # excel文档操作
        excel = code.excel_operation.ExcelOperation()
        # 将信息读入
        excel.get_data(user=self.user, account=self.account, password=self.password, real_name=self.name)
        # 在excel中将信息保存
        excel.write_new_line()

"""
完整的流程
"""
def complete_process(user = 'fzdwxxcl', username=' ', password=' '):
    link = code.linkedin_operation.Linkedin_operation(user, username, password)
    flag_have_signed_up = False
    while not flag_have_signed_up:
        try:
            link.sign_up()
            flag_have_signed_up = True
        except:
            del  link
            link = code.linkedin_operation.Linkedin_operation(user)

    flag_have_added_mailbox = False
    while not flag_have_added_mailbox:
        try:
            link.log_in()
            link.add_mail_box()
            flag_have_added_mailbox = True
        except:
            pass

    mailbox = code.mailbox_operation.Mailbox_Operation(link.driver, account=link.account,
                                                       password=link.password)

    flag_have_verified_mail = False
    while not flag_have_verified_mail:
        try:
            mailbox.log_in()
            flag_have_verified_mail = True
        except:
            print "读取邮件失败，重新打开浏览器"
            del mailbox
            link.driver.quit()
            link.driver = webdriver.Chrome()
            mailbox = code.mailbox_operation.Mailbox_Operation(link.driver, account=link.account,
                                                               password=link.password)

    flag_have_deleted_phonenumber = False
    while not flag_have_deleted_phonenumber:
        try:
            link.delete_phone_num()
            flag_have_deleted_phonenumber = True
        except:
            pass

    link.save_data()
    print "结束"

if __name__ == '__main__':
    link = Linkedin_operation()
    # link.sign_up()
    # link.log_in()
    # link.add_mail_box()

    # mailbox = code.mailbox_operation.Mailbox_Operation(link.driver)
    # mailbox.log_in()
    # link.delete_phone_num()
