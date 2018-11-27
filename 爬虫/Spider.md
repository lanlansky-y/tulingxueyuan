urllib
    包含模块
        urllib.request:打开和读取urls
        urllib.error:包含urllib.request产生的常见的错误，使用try捕捉
        urllib.parse:包含一些解析url的方法
        urllib.robotparse:解析robots.txt文件
        案例：v1.py
网页编码问题解决
    chardet:可以自动检测页面文件的编码格式，但是可能有误
    可能会需要安装 conda install chardet
    案例：v2.py
urlopen的返回对象
    案例：v3.py
    geturl:返回请求对象的url
    info:请求反馈对象的meta信息
    getcode:返回http code
    详见：案例:v3.py后半段
request.date的使用
    访问网络的两种方法
        -get：
            -利用参数给服务器传递信息
            -参数为dict， 然后用parse编码
            案例：v4.py
        -post
            -一般向服务器传递参数使用
            -post是把信息自动加密处理
            -我们如果想使用post信息，需要用到data参数
            -使用post，意味着http的请求头可能需要更改：
                Content-Type:application/x-www.form-urlencode
                Content-Length：数据长度
                简而言之，一旦更改请求方法，请注意其他请求头信息相配套
            urllib.parse.urlencode可以将字符串自动转换成上面的格式
            -案例:v5.py
            -为了更多的额设置请求信息，单纯的通过urlopen函数已经不太好用了
            -需要利用request.Request类
            案例:v6.py
urllib.error
    URLError产生的原因：
        1.没网
        2.服务器链接失败
        3.指不到指定的服务器
    是OSError的子类
    案例v7.py
    HTTPError
    案例v8.py
    HTTPError和URLError区别：
        HTTPError是对应的HTTP请求的返回码错误，如果返回码是400以上的，则引发HTTPError
        URLError对应的一般是网络出现问题，包括url错误
UserAgent
    UserAgent:用户代理，简称UA,属于heads的一部分，服务器通过UA来判断访问者身份
    常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
    设置UA可以通过两种方式：
        heads
        add_header
        案例：v9.py
ProxyHandler处理(代理服务器)
    -使用代理IP，是爬虫的常用手段
    -获取代理服务器的地址
        www.xicidaili.com
        www.goubanjia.com
    -代理用来隐藏真实访问者，代理也不允许 频繁访问某一个固定网站，所以，代理一定要很多很多
    -基本使用步骤：
        1.设置代理地址
        2.创建ProxyHandler
        3.创建Opener
        4.安装Opener
    案例：v10.py
cookie & session
    -由于http协议的无记忆性，人们为了弥补这个缺憾所采取的一个补充协议
    -cookie是发放给用户(即http浏览器)的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息
    
-cookie 和 session的区别
    -存放位置不同
    -cookie不安全
    -session会保存在服务器上一定时间
    -单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个
session的存放位置
    -存在服务器端
    -一般情况下， session是放在内存中或者数据库中
    -没有cookie登录，案例:v11.py,可以发现，没使用cookie，网页是未登录状态
    -使用cookie登录
        -直接把cookie赋值下来，然后手动放入请求头，案例:v12.py
        -http模块包含一些关于cookie的模块，通过它们，我们可以自动使用cookie
            CookieJar
                -管理存储cookie,向传出的http请求添加cookie
                -cookie存储在内存中，CookieJar实例回收后cookie将消失
            FileCookieJar(filename, delayload=None, policy=None)
                -使用文件管理cookie
                -filename是保存cookie的文件
            MozillaCookieJar(filename, delayload=None, policy=None)
                -创建与mozilla浏览器cookie.txt兼容的FileCookieJar实例
            LwpCookieJar
                -创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
            他们的关系是CookieJar-->FileCookieJar-->MozillaCookieJar & LwpCookieJar
    利用cookiejar访问网易云课堂
    案例:v13.py
        -自动使用cookie登录，大致流程是
        -打开登录页面后自动通过用户名和密码登录
        -自动提取反馈回来的cookie
        -利用提取的cookie登录隐私页面
    handler是Handler的实例，常用的参看案例13.py
        用来处理复杂请求
        #生成cookie的管理器
            cookie_handler = request.HTTPCookieProcessor(cookie)
        #创建http请求管理器
            http_handler = request.HTTPHandler()
        #生成https管理器
            https_handler = request.HTTPSHandler()
    创建handler后，使用opener打开，打开后相应的业务由相应的handler处理
    把cookie作为一个变量，打印出来，案例：v14.py
        cookie的属性
            name:名称
            value:值
            domain:可以访问此cookie的域名
            path:可以访问此cookie的页面路径
            expires:过期时间
            size:大小
            Http字段
    cookie的保存-FileCookieJar
    案例：v15.py
    cookie的读取，案例：v16.py
-SSL
    SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书(Sercure Socket Layer)
    美国网景公司开发
    CA(Certifacate Authority)是数字证书认证中心，是发放、管理、废除数字证书的收信人的第三方机构
    遇到不信任的SSL证书，需要单独处理，案例:v17(尴尬，现在的12306网站好像有官方SSL证书了)
-js加密
    -有的反爬虫策略采用js对需要传输的数据进行加密处理(通常是取md5值)
    -经过加密，传输的就是密文，但是加密函数或者过程一定是在浏览器上完成的，也就是一定会把代码(js代码)暴露给使用者
    -通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    案例：v18.py,v19.py
-ajax
    -异步请求
    -一定会有url、请求方法、可能有数据
    -一般使用json格式
    案例：v20.py
-Requests
    HTTP for Humans  比urllib更简洁，更友好
    继承了urllib的所有特征
    底层使用的是urllib3
    开源地址：https://github.com/requests/requests
    中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
    get请求
        requests.get(url)
        requests.request('get', url)
        可以带有headers和params参数
    案例：v21.py
    get返回内容
    案例：v22.py
-post
    rsp = requests.post(url, data=data)
    案例:v23.py
    data, headers要求是dict类型
-proxy
    proxies = {
        "http":"address of proxy",
        "https":"address of proxy"
        }
        rsp = requests.request("get", "http:xxxxx", proxies=proxies)
    代理有可能会报错哦，如果使用人数多，考虑安全问题，可能会被强行关闭
-用户验证
    -代理验证
        #可能需要使用HTTP basic Auth
        #格式为  用户名:密码@代理地址:端口地址
        proxy = {"http":"china:123456@192.168.1.123:4444"}
        rsp = requests.get("http://baidu.com", proxies=proxy)
-web客户端验证
    -如果遇到web客户端验证，需要添加auth=(用户名，密码)
        auth = ("test1", "123456")#授权信息
        rsp = requests.get("http://www.baidu.com", auth=auth)
-cookie
    requests可以自动处理cookie信息
    rsp = requests.get("http://xxxxx")
    #如果对方服务器传送过来cookie信息了，则可以通过反馈过来的cookie属性得到
    #返回一个cookiejar实例
    cookiejar = rsp.cookies
    
    #可以把cookiejar转换成字典
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
-session
    -跟服务器上的session不一样
    -模拟一次会话，从客户端浏览器链接服务器开始，到客户端浏览器断开
    -能让我们跨请求时保持某些参数，比如在同一个session实例发出的所有请求之间保持cookie
    #创建session对象，可以保持cookie值
    ss = requests.session()
    headers = {"User-Agent":"xxxxxxxx"}
    data = {"name":"xxxxxxx"} 
    #此时，由创建的session管理请求,负责发出请求
    ss.post("http://www.baidu.com", data=data, headers=headers)
    rsp = ss.get("xxxxx")
-https请求验证ssl证书
    -参数verify负责表示是否需要验证ssl证书，默认是True
    -如果不需要验证ssl证书，则设置成false表示关闭
    rsp = requests.get("https://www.baidu.com", verify=false)
    #如果用verify=True访问12306会报错，因为它证书有问题(不过下载可能没啥问题了)
    
    