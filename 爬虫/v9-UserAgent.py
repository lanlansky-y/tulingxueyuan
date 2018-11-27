'''
访问一个网站
更改自己的UserAgent进行伪装
'''
from urllib import request, error

if __name__ == '__main__':
    url = "https://www.baidu.com"

    try:
        '''
        #使用heads方法伪装UA
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        req = request.Request(url, headers=headers)
        '''

        #使用add_header伪装UA
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')

        #正常访问
        rsp = request.urlopen(req)
        html = rsp.read()
        html = html.decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)