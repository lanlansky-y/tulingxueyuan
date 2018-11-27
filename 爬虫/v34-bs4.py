from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

#bs会自动转码
content = soup.prettify()

#Tag
print(soup.meta)
print('=='*20)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)  #是字典格式

#NavigableString
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
print('=='*20)
#BeautifulSoup
print(soup)
print(soup.name)
print(soup.attrs)