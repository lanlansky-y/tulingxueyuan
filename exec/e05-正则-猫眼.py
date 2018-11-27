'''
利用正则来爬取猫眼电影
1.url:http://maoyan.com/board
2.把电影信息尽可能多的拿下来

分析
1.一个影片的内容是以dd开始的单元
2.在单元内存在一部电影的所有信息

思路：
1.利用re把dd内容都给找到
2.对应找到每一个dd，用re挨个查找需要的信息

方法就是三步走：
1.把页面down下来
2.提取出dd单位的内容
3.对每一个dd,进行单独信息提取
'''

from urllib import request, error

#1.下载页面内容
url = "http://maoyan.com/board"

try:
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
        'Connection': "keep-alive"
    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    # print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)

#2.把dd提取出来，缩小处理范围
import re

s = r"<dd>(.*?)</dd>"
pattern = re.compile(s, re.S)

films = pattern.findall(html)
print(len(films))
print(films[0])

#3.从每个dd里面单独提取出需要的信息
for film in films:
    #提取电影名称
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)