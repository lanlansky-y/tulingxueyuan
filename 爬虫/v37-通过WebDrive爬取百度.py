'''
通过WebDrive操作百度进行查找
'''

from selenium import webdriver
import time

import phantomjs
#通过Keys模拟键盘
from selenium.webdriver.common.keys import Keys

#操作哪个浏览器就对哪个浏览器建一个实例
#自动按照环境变量查找相应的浏览器
drive = webdriver.PhantomJS()

#如果浏览器没有在相应环境变量中，需要指定浏览器位置
drive.get("http://www.baidu.com")

#通过函数查找title标签
print("Title:{0}".format(drive.title))