'''
破解有道词典V2
处理js加密代码
'''

'''
通过查找，能找到有道翻译网页中fanyi.min.js中的Response里的代码
1.salt:  t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
2.sign:  n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK")    
    md5一共需要四个参数，第一个和第四个都是固定的字符串，第二个参数就是输入的要查找的单词，第三个参数就是所谓的salt
'''

def getSalt():
    '''
    salt的公式："" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
    需要把salt的公式翻译成python代码
    :return:
    '''
    import time, random
    salt = int(time.time()*1000) + random.randint(0, 10)

    return salt

def getMd5(v):
    import hashlib
    md5 = hashlib.md5()

    #update需要一个bytes格式的参数
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()

    return sign

def getSign(key, salt):
    sign1 = "fanyideskweb" + key + str(salt) + "6x(ZHw]mwzX#u0V7@yfwK"
    sign = getMd5(sign1)

    return sign

from urllib import request, parse

def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    salt = getSalt()
    data = {'i':key,
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt': str(salt),
            'sign': getSign(key, salt),
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