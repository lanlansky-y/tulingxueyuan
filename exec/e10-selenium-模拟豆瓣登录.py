'''
利用selenium模拟登录豆瓣
需要输入验证码
思路：
1.保存页面快照
2.等待用户手动输入验证码
3.继续自动执行提交等动作

'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

url = 'https://accounts.douban.com/login?redir=https%3A%2F%2Fbook.douban.com%2Fsubject_search%3Fsearch_text%3Dpython%26cat%3D1001%26start%3D%25s0&source=main'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(4)
#生成快照，用来查看验证码
driver.save_screenshot('douban_index.png')
captcha = input("please input your code:")

#利用账户信息和验证码登录
driver.find_element_by_id('email').send_keys('1366798119@qq.com')
driver.find_element_by_id('password').send_keys('haha123456')
driver.find_element_by_id('captcha_field').send_keys(captcha)

driver.find_element_by_name('login').click()

time.sleep(5)

driver.save_screenshot('logined.png')

driver.quit()