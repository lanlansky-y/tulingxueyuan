from http import cookiejar
from urllib import request, parse

#创建mozillacookiejar实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

#生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

#创建http请求管理器
http_handler = request.HTTPHandler()

#生成https管理器
https_handler = request.HTTPSHandler()

#创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def getHomePage():
    url = 'http://www.renren.com/965187997/profile'

    rsp = request.urlopen(url)
    html = rsp.read()
    html = html.decode()
    with open('test16.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    getHomePage()