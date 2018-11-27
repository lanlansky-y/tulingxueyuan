'''
扇贝单词：
1.把python单词列表download下来
2.主要练习的目的是xpath
3.理论上讲不需要登录
4.https://www.shanbay.com/wordlist/104899/202159/
'''

from urllib import request

from lxml import etree

import json

#词汇表
words = []

def shanBei(page):
    url = "https://www.shanbay.com/wordlist/104899/202159/?page=%s"%page
    print(url)

    rsp = request.urlopen(url)
    html = rsp.read()


    #解析html
    html = etree.HTML(html)

    tr_list = html.xpath('//tr[@class="row"]')
    # print(type(tr_list))
    # print(tr_list)

    #遍历每个tr元素，每个tr对应一个单词和解释
    for tr in tr_list:
        '''
        查找相应的单词和解释
        '''
        word = {}
        strong = tr.xpath('.//strong')
        if len(strong):
            #strip把找到的内容去掉空格
            name = strong[0].text.strip()
            word["name"] = name


        #查找单词的解释
        td_content = tr.xpath('./td[@class="span10"]')
        if len(td_content):
            content = td_content[0].text.strip()
            word['content'] = content
            print(word)

        if word != {}:
            words.append(word)
        # print(words)

if __name__ == '__main__':
    shanBei(2)