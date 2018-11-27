import scrapy
import re

from e16_qq.items import QQItem

class QQSpider(scrapy.Spider):

    name = 'qq'
    #设置爬取的范围：只能爬取hr.tencent.com域名的信息
    allowed_domains = ['hr.tencent.com']
    start_urls = [
        'https://hr.tencent.com/position.php?keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&start=0#a'
    ]

    def parse(self, response):
        #下载的结果自动放在response内存储
        for each in response.xpath('//*[@class="even"]'):
            #对于得到的每一个工作信息内容，都封装到相应的item内
            item = QQItem()
            name = each.xpath('./td[1]/a/text()').extract()[0]
            detailLink = each.xpath('./td[1]/a/@href]').extract()[0]
            positionInfo = each.xpath('./td[2]/text()').extract()[0]
            workLocation = each.xpath('./td[4]/text()').extract()[0]

            item['name'] = name.encode('utf-8')
            item['detailLink'] = detailLink.encode('utf-8')
            item['positionInfo'] = positionInfo.encode('utf-8')
            item['workLocation'] = workLocation.encode('utf-8')

            yield item