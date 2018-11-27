# _*_ coding:utf-8 _*_
from urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"
    req = request.Request(url)

    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open('test.html', 'w+', encoding='utf-8') as ts:
        ts.write(html)