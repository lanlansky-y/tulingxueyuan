from urllib import request

'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''

if __name__ == '__main__':
    url = 'https://study.163.com/my'
    #打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)
    #把返回的结果读取出来
    html = rsp.read()
    #这样读取出来的内容类型为bytes
    print(type(html))
    print(html)
    #如果想把bytes内容转换成字符串，需要解密
    html = html.decode()
    print(html)