from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')
tag = soup.prettify()
print(tag)
print("=="*20)
print(soup.title.string)
print(soup.select('title'))
print("=="*20)

metas = soup.select('meta[content="always"]')
print(metas)
