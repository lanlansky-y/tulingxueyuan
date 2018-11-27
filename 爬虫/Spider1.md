#页面解析和数据提取
    -结构数据：注重先有结构再谈数据
        -JSON文件
            -JSON Path
            -转换成python类型进行操作(json类)
        -XML文件
            -转换成Python类型(xml to dict)
            -XPath
            -CSS选择器
            -正则
    -非结构化数据：先有数据再谈结构
        -比如说文本、电话号码、邮箱地址
        -通常处理此类数据使用正则表达式
        -html文件
            -正则
            -Xpath
            -CSS选择器
        
##正则表达式
    -一套规则，可以在字符串文本中进行搜查替换等
    -案例:v24.py re的基本使用流程
    -案例:v25.py match的基本使用
    -正则常用方法;
        match:从开始位置开始查找，如果不是起始位置匹配成功的话，match()就返回none,如果匹配到符合条件的也不会再进行查找了
        search:扫描整个字符串并返回第一个成功的匹配,也可以指定查找的起始范围。案例：v26.py
        findall:查找全部符合条件的组合，返回列表。案例：v27.py
        finditer:全部匹配，返回迭代器。案例：v27.py
        split:分割字符串，返回列表
        sub:替换
    -匹配中文
        -中文unicode范围主要在[u4e00-u9fa5]
        -案例：v28.py
    -贪婪与非贪婪模式
        -贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配
        -非贪婪模式：在整个表达式匹配成功的前提下，只匹配一次
        python里面数量词默认是贪婪模式
        -例如
            查找文本abbbbbbccc
            re是ab*
            贪婪模式下结果是abbbbbb
            非贪婪模式下结果是a
##XML
    XML(extensible Markup Language)
    http://www.w3school.com.cn/xml/index.asp
    案例：v29.xml
##XPath
    XPath(XML Path Language),是一门在XML文档中查找信息的语言
    官方文档：http://www.w3school.com.cn/xpath/index.asp
    XPath开发工具
        -开源的XPath表达式工具:XMLQuire
        -chrome插件：XPath Helper
        -Firefox插件：XPath Checker
    -常用的路径表达式：
        nodename:选取此节点的所有子节点
        /: 从根节点选取
        //:从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
        .: 当前节点
        ..:父节点
        @:选取属性
        案例：
            路径表达式           结果
            bookstore       选取 bookstore 元素的所有子节点。
            /bookstore      选取根元素 bookstore。(注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！)
            bookstore/book  选取属于 bookstore 的子元素的所有 book 元素。
            //book          选取所有 book 子元素，而不管它们在文档中的位置。
            bookstore//book 选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
            //@lang         选取名为 lang 的所有属性。
        谓语(Predicates)
            -谓语用来查找某个特定的节点，写在方括号中
            例如：/bookstore/book[1]:选取第一个属于bookstore元素的子元素book。
                 /bookstore/book[last()]:选取最后一个属于bookstore元素的子元素book。
                 /bookstore/book[last()-1]:选取倒数第二个属于bookstore元素的子元素book。
                 /bookstore/book[position()<3]:选取属于bookstore元素的子元素book的前两个元素。
                 /bookstore/book[@lang="cn"]:选取属于bookstore下叫book的含有属性lang等于cn的元素。
                 /bookstore/book[@price<90]:选取属于bookstore下叫booke的含有属性price的，且属性值小于90的元素。
                 /bookstore/book[@price<90]/title:选取属于bookstore下叫book的含有属性price的且属性值小于90的元素的子元素title。
        通配符
            *：任何元素节点
            @*：匹配任何属性节点
            node():匹配任何类型的节点
        选取多个路径
            //book/title | //book/author:选取book元素中的title和author元素
            //title | //price:选取文档中所有的title和price元素
##lxml库
    python的HTML/XML的解析器
    官方文档：http://lxml.de/index.html
    功能：
        解析HTML   案例：v29.py
        文件读取(只能读取xml文件)   案例：v30.xml, v31.py
        etree和XPath的配合使用，案例v32.py
#CSS选择器(Beautiful Soup4)
    首先需要安装
    官网：http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
    几个常用提取信息工具的比较“
        正则：很快，不好用，无需安装
        beautifulsoup：慢，使用简单，安装简单
        lxml：比较快，使用简单，安装一般
    案例：v33.py
    四大对象：
        Tag
        NavigableString
        BeautifulSoup
        Comment
    Tag:
        对应html中的标签
        可以通过soup.tag_name(标签名字)
        tag的两个重要属性
            name
            attrs
        案例:v34.py
    NavigableString
        对应内容值
    BeautifulSoup
        表示的是一个文档的内容，大部分的时候可以把他当作tag对象
        一般我可以用soup表示
    Comment
        特殊类型的NavigableString对象
        对其输出，则内容不包括注释符号
    遍历文档对象
        contents:tag的子节点以列表的方式给出
        children:子节点以迭代器形式返回
        descendants:所有子孙节点
    搜索文档对象
        find_all(name, attrs, recursive, text, **kwargs)
            name:按照字符串搜索，可以传入的内容为
                -字符串
                -正则
                -列表
            keyword参数，主要用来表示属性
            text:对象tag的文本值
            案例：v35.py
##css选择器
    使用soup.select,返回一个列表
    通过标签名称查找：soup.select("title")
    通过类名查找：soup.select(".content")
    通过id查找：soup.select("#name_id")
    通过组合查找：soup.select("div #input_content")
    通过属性查找：soup.select('img[class="photo"]')
    获取tag内容：tag.get_text
    案例:v36.py