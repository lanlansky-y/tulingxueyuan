'''
构建代理集群/队列
每次访问服务器，随机抽取一个代理
抽取可以使用random.choice

分析步骤：
1.构建代理群
2.每次访问，随机选取代理并执行
'''

proxy_list = [
    #列表中存放的是dict类型的元素
    {"http":"39.107.76.192"},
    {"http":"112.115.163.76"},
    {"http":"115.223.231.226"},
    {"http":"1.202.122.239"}

]

from urllib import request, error
import random


url = "http://www.zjlipo.com/"

'''
#方法一
#创建ProxyHandler
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)
#创建Opener
opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)
'''


#方法二
opener_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)


try:
    opener = random.choice(opener_list)
    request.install_opener(opener)

    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)