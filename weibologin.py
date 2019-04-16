# -*- coding:utf-8 -*-
#浏览器引擎类
import configparser
import os.path
import time

from selenium import webdriver

from supertopicSignin import click_submit


class weiboLogin(object):

    config = configparser.ConfigParser()
    config.read("F:\\个人文档\\code\\Kumapocket\\config\\config.ini")
    username = config.get("userName", "userName")
    password = config.get("passWord", "PassWord")



    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,driver,username = username,password = password):

        PostUrl = "https://passport.weibo.cn/signin/login"
        # 用浏览器实现访问
        self.driver = webdriver.Chrome()
        driver.get(PostUrl)

        # 输入账号密码
        self.driver.find_element_by_id('loginName').send_keys(username)
        self.driver.find_element_by_id('loginPassword').send_keys(password)

        # 点击登录
        self.driver.find_element_by_id('loginAction').click()
        click_submit.click()
        time.sleep(5)

    def quit_browser(self):
        self.driver.quit()