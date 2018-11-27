'''
要求导入scrapy
所有类的命名一般是xxxSpider
所有的爬虫类都是scrapy.spider的子类
'''
import scrapy


class BaiduSpider(scrapy.Spider):
    #name是爬虫的名称
    name = 'baidu'

    #起始url列表
    start_urls = ['http://www.baidu.com']

    #parse负责分析download下载得到的结果
    def parse(self, response):
        '''
        只是保存网页即可
        :param response:
        :return:
        '''
        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))