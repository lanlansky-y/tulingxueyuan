from urllib import request
from bs4 import BeautifulSoup
import re

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

print('=='*20)
tags = soup.find_all(name='meta')
print(tags)
print('=='*20)
tags1 = soup.find_all(re.compile('^me'))
if tags == tags1:
    print(True)

for i in tags1:
    print(i)

print('=='*20)
print(soup.find_all(re.compile('^me'), content="always"))