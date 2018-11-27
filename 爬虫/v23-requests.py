import requests
from urllib import parse

import json

baseurl = "https://fanyi.baidu.com/sug"
c1 = input("请输入一个单词：")
#存放模拟form的数据一定是dict格式
data = {"kw": c1}

#需要使用parse模块对data进行编码
# data = parse.urlencode(data)
# print(type(data))
# data = data.encode('utf-8')
# print(type(data))


#我们需要构造一个请求头,请求头应该至少包含传入的数据的长度
#request要求传入的请求头是一个dict格式
headers = {
    #因为使用post，至少应该包含Content-Length字段
    'Content-Length':str(len(data))
}

#有了headers,data,url之后就可以尝试发出请求了
#data要是dict格式
rsp = requests.post(baseurl, data=data, headers=headers)
print(rsp.text)
print(rsp.json())

# #用json把字符串转换成字典
# json_data = json.loads(json_data)
# print(json_data)
# print(type(json_data))
#
# #返回的json_data是一个字典
# for i in json_data['data']:
#     print(i['k'], '--', i['v'])