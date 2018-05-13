# -*- coding:utf-8 -*-
__author__ = 'LZ'

import code.setname
import code.Phone_api
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')


"""
实现126邮箱相关的操作
"""
class Mailbox_Operation(object):
    def __init__(self, driver, account='huangjiao807676546@126.com', password='hei38803'):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
        self.account = account
        self.password = password

    """
    登陆邮箱，并读取邮件，点击其中的验证链接
    """
    def log_in(self):
        driver = self.driver
        driver.get('http://reg.163.com/')
        time.sleep(1)
        frame = driver.find_element_by_tag_name('iframe')
        # print frame
        frame_father = driver.find_element_by_class_name('zj-login')
        # print"found zj-login!"
        iframe = frame_father.find_element_by_tag_name('iframe')
        # iframe = driver.find_element_by_xpath('//*[@id="x-URS-iframe1526110797407.0286"]')
        driver.switch_to_frame(iframe)  # 登录页面存在iframe
        # driver.find_element_by_class_name('j-inputtext dlemail').clear()
        driver.find_element_by_name('email').send_keys(self.account)
        driver.find_element_by_name('password').send_keys(self.password, Keys.ENTER)
        time.sleep(1)  # 跳转页面时，强制等待6s

        account_main_url = 'http://reg.163.com/Main.jsp'

        flag_has_loggeg_in = False
        while not flag_has_loggeg_in:
            time.sleep(0.5)
            current_url = driver.current_url
            if current_url == account_main_url:
                flag_has_loggeg_in = True

        # driver.get('http://mail.126.com/')
        time.sleep(0.5)
        try:
            driver.find_element_by_class_name('i-app-close').click()
        except:
            pass
        try:
            driver.find_element_by_class_name('r_btn').click()
        except:
            pass
        time.sleep(0.5)
        iframe = driver.find_element_by_xpath('//*[@id="v1"]/div[1]/iframe')
        driver.switch_to_frame(iframe)
        # WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, 'webmail')))
        button_sign_in = driver.find_element_by_xpath('//*[@id="webmail"]')
        button_sign_in.click()

        all_handles = driver.window_handles
        # print all_handles
        current_handle = driver.current_window_handle
        #切换到下一个标签页
        handle_id = 0
        for handle in all_handles:
            if current_handle == handle:
                driver.switch_to_window(all_handles[handle_id + 1])
                break
            else:
                handle_id += 1

        #进入收信页面
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.CLASS_NAME, 'oz0')))
        button_recieve = driver.find_element_by_class_name('oz0')
        button_recieve.click()

        time.sleep(1)
        WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.rF0.kw0.nui-txt-flag0')))
        last_letter = driver.find_element_by_css_selector('div.rF0.kw0.nui-txt-flag0')
        last_letter.click()

        time.sleep(0.5)
        WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.CLASS_NAME, 'nu0')))
        iframe = driver.find_element_by_class_name('nu0').find_element_by_tag_name('iframe')
        driver.switch_to_frame(iframe)
        # print iframe
        email_text = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td/table[5]/tbody/tr/td[2]/table[2]/tbody/tr[3]/td')
        # print email_text
        activate_link = email_text.find_element_by_tag_name('a')
        activate_link.click()
        #  activate_link.get_attribute('href')

        time.sleep(3)
        # driver.quit()


if __name__ == '__main__':
    mailbox = Mailbox_Operation()
    mailbox.log_in()