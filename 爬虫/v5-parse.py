from urllib import request, parse
'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
1.打开F12
2.尝试输入girl，每次敲一个字母后都有请求
3.请求地址是http://fanyi.baidu.com/sug
4.查看NteWork-All-Headers,发现FormData的值是kw:girl
5.检查返回内容格式，发现返回的是json格式内容-->需要用到json包
'''
import json
'''
大致流程是
1.利用data构造内容，然后urlopen打开
2.返回一个json格式的结果
3.结果就应该是girl的释义
'''
baseurl = "https://fanyi.baidu.com/sug"
c1 = input("请输入一个单词：")
#存放模拟form的数据一定是dict格式
data = {"kw": c1}

#需要使用parse模块对data进行编码
data = parse.urlencode(data)
print(type(data))
data = data.encode('utf-8')
print(type(data))

'''
很遗憾，headers没有用到
#我们需要构造一个请求头,请求头应该至少包含传入的数据的长度
#request要求传入的请求头是一个dict格式
headers = {
    #因为使用post，至少应该包含Content-Length字段
    'Content-Length':len(data)
}
'''
#有了headers,data,url之后就可以尝试发出请求了
rsp = request.urlopen(baseurl, data=data)
json_data = rsp.read().decode('utf-8')
print(json_data)
print(type(json_data))
#用json把字符串转换成字典
json_data = json.loads(json_data)
print(json_data)
print(type(json_data))

#返回的json_data是一个字典
for i in json_data['data']:
    print(i['k'], '--', i['v'])