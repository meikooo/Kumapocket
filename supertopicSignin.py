# -*- coding: utf-8 -*-
from selenium import webdriver
import time

#打开马嘉祺超话链接
PostUrl = "https://m.weibo.cn/p/100808d084599a8d651890c335344604dc6441"
# 用浏览器实现访问
driver = webdriver.Chrome()
driver.get(PostUrl)

#webdriver休眠一段时间来slow down测试代码的执行速度，强制driver等待一个固定的时间来让元素加载完成
time.sleep(2)
elem_add = driver.find_element_by_class_name('m-add-box').click()
time.sleep(2)
ele_login = driver.find_element_by_link_text('登录').click()
time.sleep(2)
# 账号填充输入
driver.switch_to.default_content()
elem_user = driver.find_element_by_id('loginName').send_keys('aa@qq.com')
elem_password = driver.find_element_by_id('loginPassword').send_keys('aa')

#点击登录
click_submit = driver.find_element_by_id('loginAction')
click_submit.click()
time.sleep(5)
#点击签到
elem_addd = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/h4').click()
time.sleep(5)
#张真源超话链接
ZhangUrl="https://m.weibo.cn/p/1008081631871d44bb53c07db75a5ef288af6a/"
driver.get(ZhangUrl)
time.sleep(5)
#点击签到
elem_addd = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/h4').click()
time.sleep(2)
