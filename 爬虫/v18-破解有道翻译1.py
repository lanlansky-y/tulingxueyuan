'''
破解有道词典V1
'''

from urllib import request, parse

def youdao(key):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    data = {'i':key,
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt':'1541571368941',
            'sign':'8567b4df786b7c913b4102d0d71ead4f',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_REALTIME',
            'typoResult':'false'
    }

    #参数data需要是bytes格式
    data = parse.urlencode(data)
    data = data.encode()

    headers = {'Accept':'application/json,text/javascript,*/*;q=0.01',
                #'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.9',
                'Connection':'keep-alive',
                'Content-Length':'197',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie':'OUTFOX_SEARCH_USER_ID=799059865@115.216.13.185;__guid=204659719.2018781846773936400.1536634036426.1697;_ntes_nnid=5200b867a2d0529f412799b764a48997,1536634036505;P_INFO=yyz865676567;JSESSIONID=aaaOEzrAiLl_sabZCZSBw;OUTFOX_SEARCH_USER_ID_NCOO=1301263500.2590437;monitor_count=4;___rl__test__cookies=1541571368931',
                'Host':'fanyi.youdao.com',
                'Origin':'http://fanyi.youdao.com',
                'Referer':'http://fanyi.youdao.com/',
                'User-Agent':'Mozilla/5.0(Windows NT6.1;WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/63.0.3239.132 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'}
    req = request.Request(url, data=data, headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao('boy')