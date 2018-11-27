#动态HTML
##爬虫跟反爬虫
    JavaScript
    jQuery
    ajax
    DHTML
    Python采集动态数据
        从JavaScript代码入手采集
        Python第三方库运行JavaScript直接采集你在浏览器看到的页面
##Selenium + PhantomJS
    Selenium:web自动化测试工具
        自动加载页面
        获取数据
        截屏
        官网：http://selenium-python.readthedocs.io/index.html
    PhantomJS(幽灵浏览器)
        基于Webkit的无界面的浏览器
        官网：http://phantomjs.org/download.html
    Selenium库有一个WebDrive的API
    WebDrive可以跟页面上的元素进行各种交互，用它可以来进行爬取
    案例：v37.py
    Selenium操作主要分两大类：
        得到UI元素
            find_element_by_id
            find_elements_by_name
            find_elements_by_xpath
            find_elements_by_link_text
            find_elements_by_partial_link_text
            find_elements_by_tag_name
            find_elements_by_class_name
            find_elements_by_css_selector
        基于UI元素操作的模拟
            单击
            右键
            拖拽
            输入
            可以通过导入ActionsChains类来做到
        案例：v38.py
    chrome + chromedriver
        -下载安装chrome
        -下载安装chromedriver
    一些linux系统下的操作：
        dpkg -L xxxx：查找下载的xxxx文件安装位置
        ./xxxx：     直接运行xxxx文件
        bash xxxx：  运行xxxx文件