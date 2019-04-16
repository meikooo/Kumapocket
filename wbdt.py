# -*- coding: utf-8 -*-
import configparser
# python3.6环境
from urllib import request
from http import cookiejar
import os
from selenium import webdriver
import time

#进入到搜索页
gqtPostUrl="https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E5%85%B1%E9%9D%92%E5%9B%A2%E4%B8%AD%E5%A4%AE"
# 用浏览器实现访问
driver = webdriver.Chrome()
driver.get(gqtPostUrl)
time.sleep(3)
#webdriver休眠一段时间来slow down测试代码的执行速度，强制driver等待一个固定的时间来让元素加载完成
elem_add = driver.find_element_by_class_name('m-add-box').click()

ele_login = driver.find_element_by_link_text('登录').click()
time.sleep(2)
driver.switch_to.default_content()
#将账号密码输入到config文件中，提交代码至GitHub时忽略config文件
config = configparser.ConfigParser()
config.read("F:\\个人文档\\code\\Kumapocket\\config\\config.ini")
username = config.get("userName", "userName")
password = config.get("passWord", "PassWord")

# 输入账号密码
elem_user = driver.find_element_by_id('loginName').send_keys(username)
elem_password = driver.find_element_by_id('loginPassword').send_keys(password)

#点击登录
click_submit = driver.find_element_by_id('loginAction')
click_submit.click()
time.sleep(10)

#关注共青团
gqtPostUrl="https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E5%85%B1%E9%9D%92%E5%9B%A2%E4%B8%AD%E5%A4%AE"
driver.get(gqtPostUrl)
time.sleep(3)
elem_add = driver.find_element_by_class_name('m-add-box').click()

#关注姚明明
ymmUrl="https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E5%A7%9A%E6%98%8E%E6%98%8E"
driver.get(ymmUrl)
time.sleep(6)
elem_add = driver.find_element_by_class_name('m-add-box').click()

#点赞
aUrl="https://m.weibo.cn/detail/4360772106535790"
driver.get(aUrl)
time.sleep(3)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
bUrl="https://m.weibo.cn/detail/4360406401779766"
driver.get(bUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
cUrl="https://m.weibo.cn/detail/4358480263588497"
driver.get(cUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
dUrl="https://m.weibo.cn/detail/4358139237227100"
driver.get(dUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
eUrl="https://m.weibo.cn/detail/4357869992406592"
driver.get(eUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
fUrl="https://m.weibo.cn/detail/4356363197212833"
driver.get(fUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
gUrl="https://m.weibo.cn/detail/4355548541794251"
driver.get(gUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
hUrl="https://m.weibo.cn/detail/4355288058742660"
driver.get(hUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
lUrl="https://m.weibo.cn/detail/4352759257467585"
driver.get(lUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
mUrl="https://m.weibo.cn/detail/4351596123094850"
driver.get(mUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
gUrl="https://m.weibo.cn/detail/4350219095247355"
driver.get(gUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
hUrl="https://m.weibo.cn/detail/4349698553029765"
driver.get(hUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
lUrl="https://m.weibo.cn/detail/4347628860233224"
driver.get(lUrl)
time.sleep(2)
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()
#查看点赞互动值
numberUrl="https://m.weibo.cn/p/index?containerid=2313533137220457_-_STAR&luicode=10000011&lfid=2302833137220457"
driver.get(numberUrl)
time.sleep(2)
hudongzhi = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/h3').text
print("点赞互动值是"+hudongzhi)


# postwb="https://m.weibo.cn/compose/"
# driver.get(postwb)
# driver.find_element_by_class_name('m-wz-def').send_keys("1.张PD http://t.cn/E6bNUln益2.李老师 http://t.cn/E6AmdJz益1.公益同行 https://m.weibo.cn/3137220457/4325826218566655益2.河南范县 https://m.weibo.cn/3137220457/4339929176035884益3.蒋大为老师 https://m.weibo.cn/3137220457/4347628860233224益4.废水瓶 https://m.weibo.cn/3137220457/4349698553029765")
# time.sleep(3)
# elem_add = driver.find_element_by_class_name('m-send-btn').click()

#停留15s
txUrl="https://m.weibo.cn/detail/4325826218566655"
driver.get(txUrl)
time.sleep(15)
hnUrl="https://m.weibo.cn/detail/4339929176035884"
driver.get(hnUrl)
time.sleep(15)
jdwUrl="https://m.weibo.cn/detail/4347628860233224"
driver.get(jdwUrl)
time.sleep(15)
jspUrl="https://m.weibo.cn/detail/4349698553029765"
driver.get(jspUrl)
time.sleep(15)

#回复PD们
pdreUrl="https://m.weibo.cn/detail/4358512156920187?cid=4358582604558850"
driver.get(pdreUrl)
current_time = time.strftime('%Y%m%d-%H%M', time.localtime(time.time()))
time.sleep(5)
postwb = driver.find_element_by_class_name('lite-page-editor').send_keys(r"加油1")
driver.find_element_by_class_name('btn-send').click()

lrhrepdUrl="https://m.weibo.cn/detail/4358233164544814?cid=4358583665767265"
current_time1 = time.strftime('%Y%m%d-%H%M', time.localtime(time.time()))
driver.get(lrhrepdUrl)
time.sleep(3)
driver.find_element_by_class_name('lite-page-editor').send_keys(r"加油2")
driver.find_element_by_class_name('btn-send').click()

#查看互动值
numberUrl="https://m.weibo.cn/p/index?containerid=2313533137220457_-_STAR&luicode=10000011&lfid=2302833137220457"
driver.get(numberUrl)
time.sleep(2)
hudongzhi = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/h3').text
print("评论点赞PD互动值是"+hudongzhi)



#回复
dxy="https://m.weibo.cn/compose/reply?id=4360772106535790&reply=4360781531296921&content=%E5%9B%9E%E5%A4%8D%40UNINE_%E5%A7%9A%E6%98%8E%E6%98%8E%3A"
driver.get(dxy)
time.sleep(5)
driver.find_element_by_class_name('textarea-box').send_keys("111热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

smz="https://m.weibo.cn/compose/reply?id=4360406401779766&reply=4360441524274855&content=%E5%9B%9E%E5%A4%8D%40UNINE_%E5%A7%9A%E6%98%8E%E6%98%8E%3A"
driver.get(smz)
time.sleep(5)
driver.find_element_by_class_name('textarea-box').send_keys("222热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

ly="https://m.weibo.cn/compose/reply?id=4360406401779766&reply=4360441607601435&content=%E5%9B%9E%E5%A4%8D%40UNINE_%E5%A7%9A%E6%98%8E%E6%98%8E%3A"
driver.get(ly)
time.sleep(5)
driver.find_element_by_class_name('textarea-box').send_keys("333热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

sxxly="https://m.weibo.cn/compose/reply?id=4360406401779766&reply=4360428354250897&content=%E5%9B%9E%E5%A4%8D%40UNINE_%E5%A7%9A%E6%98%8E%E6%98%8E%3A"
driver.get(sxxly)
time.sleep(5)
driver.find_element_by_class_name('textarea-box').send_keys("444热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

dxy2="https://m.weibo.cn/compose/reply?id=4360406401779766&reply=4360429243154808&content=%E5%9B%9E%E5%A4%8D%40UNINE_%E5%A7%9A%E6%98%8E%E6%98%8E%3A"
driver.get(dxy2)
time.sleep(5)
driver.find_element_by_class_name('textarea-box').send_keys("555热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

wyc="https://m.weibo.cn/compose/reply?id=4360406401779766&reply=4360639436691583&content=%E5%9B%9E%E5%A4%8D%40UNINE_%E5%A7%9A%E6%98%8E%E6%98%8E%3A"
driver.get(wyc)
time.sleep(5)
driver.find_element_by_class_name('textarea-box').send_keys("666热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

ljy="https://m.weibo.cn/compose/reply?id=4360406401779766&reply=4360672160946081&content=%E5%9B%9E%E5%A4%8D%40UNINE_%E5%A7%9A%E6%98%8E%E6%98%8E%3A"
driver.get(ljy)
time.sleep(5)
driver.find_element_by_class_name('textarea-box').send_keys("777热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

unine="https://m.weibo.cn/compose/reply?id=4360406401779766&reply=4360639813743922&content=%E5%9B%9E%E5%A4%8D%40UNINE_%E5%A7%9A%E6%98%8E%E6%98%8E%3A"
driver.get(unine)
time.sleep(5)
driver.find_element_by_class_name('textarea-box').send_keys("888热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

kc="https://m.weibo.cn/compose/reply?id=4360406401779766&reply=4360790720413907&content=%E5%9B%9E%E5%A4%8D%40UNINE_%E5%A7%9A%E6%98%8E%E6%98%8E%3A"
driver.get(kc)
time.sleep(5)
driver.find_element_by_class_name('textarea-box').send_keys("999热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

#查看互动值
numberUrl2="https://m.weibo.cn/p/index?containerid=2313533137220457_-_STAR&luicode=10000011&lfid=2302833137220457"
driver.get(numberUrl2)
time.sleep(5)
hudongzhi2 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/h3').text
print("评论点赞PD互动值是"+hudongzhi2)

#11个转发评论
aashl="https://m.weibo.cn/compose/repost?id=4360772106535790"
driver.get(aashl)
time.sleep(3)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("111999热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#//@UNINE_姚明明:[加油]跟我一起穿过&amp;quot;撒哈拉沙漠&amp;quot; #遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()


bbdqt="https://m.weibo.cn/compose/repost?id=4360406401779766"
driver.get(bbdqt)
time.sleep(3)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("2222999热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()

xdks="https://m.weibo.cn/compose/repost?id=4358480263588497"
driver.get(xdks)
time.sleep(3)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("333999热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()


wsymm="https://m.weibo.cn/compose/repost?id=4358139237227100"
driver.get(wsymm)
time.sleep(3)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("444999热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#//@UNINE_姚明明:我是姚明明，各位青春制作人，#青春有你#，感谢同行！")
driver.find_element_by_class_name('m-send-btn').click()
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()

hzwt="https://m.weibo.cn/compose/repost?id=4357869992406592"
driver.get(hzwt)
time.sleep(3)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("555999热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()

qrjmh="https://m.weibo.cn/compose/repost?id=4356363197212833"
driver.get(qrjmh)
time.sleep(3)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("666999热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()

sjhk="https://m.weibo.cn/compose/repost?id=4355288058742660"
driver.get(sjhk)
time.sleep(6)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("888999热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()

drxy="https://m.weibo.cn/compose/repost?id=4355548541794251"
driver.get(drxy)
time.sleep(5)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("777热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()

rebuild="https://m.weibo.cn/compose/repost?id=4352759257467585"
driver.get()
time.sleep(7)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("999热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()

dhs="https://m.weibo.cn/compose/repost?id=4351596123094850"
driver.get(dhs)
time.sleep(5)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("10000热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#//@UNINE_姚明明:#阅好书阅青春# #青春有你#  各位青春制作人和我一起来读《和这个世界温柔地对抗》吧~[太阳]")
driver.find_element_by_class_name('m-send-btn').click()
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()

yzb="https://m.weibo.cn/compose/repost?id=4350219095247355"
driver.get(yzb)
time.sleep(10)
driver.find_element_by_class_name('m-checkbox').click()
driver.find_element_by_class_name('m-wz-def').send_keys("9111热爱祖国(⑉°з°)-♡#正能量偶像姚明明#1#遇见美好#")
driver.find_element_by_class_name('m-send-btn').click()
elem_add = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[5]/div/div[2]/i[2]').click()


#查看最终互动值
numberUrl="https://m.weibo.cn/p/index?containerid=2313533137220457_-_STAR&luicode=10000011&lfid=2302833137220457"
driver.get(numberUrl)
time.sleep(2)
hudongzhi = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/h3').text
print("点赞互动值是"+hudongzhi)