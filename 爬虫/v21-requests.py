import requests

#两种请求方式
#1.使用get请求
url = 'http://www.baidu.com'
rsp = requests.get(url)

print(rsp.text)

#2.使用request请求
rsp1 = requests.request('get', url)
print(rsp1.text)