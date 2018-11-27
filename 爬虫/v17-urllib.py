from urllib import request

import ssl

url = 'https://www.12306.cn/mormhweb/'
rsp = request.urlopen(url)
html = rsp.read().decode()

print(html)