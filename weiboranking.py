import unittest
from selenium import webdriver
from weibologin import weiboLogin
import time

class weiborankingCase(unittest.TestCase):
     #
     # def setUp(self):
     #     self.dr = webdriver.Chrome()
     #     #self.dr.maximize_window()

     @classmethod
     def setUpClass(cls):
         browser = weiboLogin(cls)
         cls.driver = browser.open_browser(cls)
         time.sleep(2)

     @classmethod
     def tearDownClass(cls):
         cls.driver.quit()

     #定义登录方法
     def test_share(self):
         #微博登录页面
        #  self.dr.get('https://passport.weibo.cn/signin/login')
        #  # 输入账号密码
        #  time.sleep(5)
        #  self.dr.find_element_by_id('loginName').send_keys("3368572938@qq.com")
        #  self.dr.find_element_by_id('loginPassword').send_keys("jackson1128")
        # # 点击登录
        #  click_submit = self.dr.find_element_by_id('loginAction')
        #  click_submit.click()
         time.sleep(5)
         self.driver.get('https://m.weibo.cn/p/index?containerid=10151501_64242119&url_type=&object_type=audio&pos=1&luicode=10000011&lfid=2311401631871d44bb53c07db75a5ef288af6a__6447519824_-_userpostlist')
         time.sleep(5)
         self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/h4').click()
         time.sleep(1)
         elem_add = self.driver.find_element_by_class_name('m-send-btn').click()
         time.sleep(5)
         self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div/h4').click()
         time.sleep(1)
         elem_add = self.driver.find_element_by_class_name('m-send-btn').click()

