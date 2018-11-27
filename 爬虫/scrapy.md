#scrapy(爬虫框架)
    爬虫框架
        scrapy
        pyspider
        crawley
    scrapy框架介绍
        官方网站：http://doc.scrapy.org/en/latest/
        中文网站：http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
        安装：pip
        windows上安装的话 需要先安装Visual C ++ Build Tools 2015：
            安装网址：https://blogs.msdn.microsoft.com/pythonengineering/2016/04/11/unable-to-find-vcvarsall-bat/
    scrapy概述
        包含各个部件
            ScrapyEngine:神经中枢，大脑，核心
            Scheduler调度器：引擎发来的request请求，调度器需要处理，然后交换引擎
            Downloader下载器：用引擎发来的requests发出请求，得到response
            Spider爬虫：负责把下载器得到的网页/结果进行分解，分解成数据+链接
            ItemPipeline管道：详细处理Item
            DownloaderMiddleware下载中间件：自定义下载的功能扩展组件
            SpiderMiddleware爬虫中间件：对spider进行功能扩展
    爬虫项目大概流程
        新建项目：scrapy startproject xxx  #在终端中输入
        明确需要目标/产出：编写item.py
        制作爬虫：地址：spider/xxspider.py
        存储内容：pipelines.py    
    ItemPipeline
        对应的是pipelines文件
        爬虫提取出数据存入item后，item中保存的数据需要进一步处理，比如清晰，去重，存储等
        pipeline需要处理process_item函数
        process_item:
            spider提取出来的item作为参数传入，同时传入的还有spider
            此方法必须实现
            必须返回一个Item对象，被丢弃的item不会被之后的pipeline处理
        __init__:构造函数
            进行一些必要的参数初始化        
        open_spider(spider):
            spider对象被开启的时候调用
        close_spider(spider):
            当spider对象被关闭的时候调用
    spider
        对应的是文件夹spiders下的文件
        
    案例：e14-scrapy-baidu.py(exec)
        利用最简单的爬虫
        爬取百度页面
        关闭配置机器人协议
        scrapy startproject baidu
        scrapy crawl baidu
    案例：e15-meiju
        -创建新项目:scrapy startproject e15_meiju
        -分析网页，确定需要的内容，定义item
        -编写pipeline,确定如何处理item
        -编写spider，确定如何提取item
        -在settings.py中设置pipelines
        -可以通过增加一个单独命令文件的方式在pycharm中启动爬虫
    案例：e16_qq招聘
        -创建项目
        -编写item
        -编写spider
        -编写pipeline
        -设置pipeline