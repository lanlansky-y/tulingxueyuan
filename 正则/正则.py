#re使用大致步骤
#1.使用compile将表示正则的字符串编译为一个pattern对象
#2.通过pattern对象提供一系列方法对文本进行查找匹配，获得匹配结果，一个Match对象
#3.最后使用Match对象提供的属性嗯哼方法获得信息，根据需要进行操作
#re常用函数
#group()：获得一个或者多个分组匹配的字符串，当要获得整个匹配的子串时，直接使用group或者group()
#start()：获取分组匹配的子串在整个字符串中的起始位置，参数默认为0
#end():获取分组匹配的子串在整个字符串中的结束位置，默认为0
#span()：返回的结构技术(start(group), end(group))

import re
#查找数字
#r表示字符串不转义
p = re.compile(r'\d+')

#在字符串'one12twothree334456four78'中进行查找，按照规则p制定的正则进行查找
#返回结果是None表示没有找到，否则会返回match对象
m = p.match('one12twothree334456four78', 3, 26) #3,26表示搜索的索引范围
print(m)

#上述代码说明1.match可以输入参数表示起始位置和结束位置，2.查找到的结果只包含一个，表示第一次进行匹配成功的内容
print(m[0]) #m中只有一个值
print(m.start())    #表示查找到的结果在原字符串中所在的起始索引位置
print(m.end())      #表示查找到的结果在原字符串中所在的结束索引位置

#I表示忽略大小写
p1 = re.compile(r'([a-z]+) ([a-z]+)', re.I)

m1 = p1.match("I am really love wangxiaojing")
print(m1)
print(m1.group(0))  #表明整个结果
print(m1.start(0))
print(m1.end(0))
print(m1.group(1))
print(m1.start(1))
print(m1.end(1))
print(m1.group(2))
print(m1.start(2))
print(m1.end(2))
print(m1.groups())

#查找:search(str[, pos[, endpos]]):在字符串中查找匹配，pos和endpos表示起始位置
#findall:查找所有
#finditer:查找，返回一个iter结果
p2 = re.compile(r'\d+')
m2 = p2.search('one12two34three567four')

print(m2.group())

rst = p2.findall('one12two34three567four')
print(type(rst))
print(rst)

#sub：替换
#sub(repl, str[, count])
#sub替换的案例
p3 = re.compile(r'(\w+) (\w+)')
s = 'hello 123 wang 456 xiaojing, i love me'

rst1 = p3.sub('hello world', s)
print(rst1)

#匹配中文，大部分中文内容表示范围是[u4e00-u9fa5]，不包括全角标点
title = u'世界 你好， hello moto'

p4 = re.compile(r'[\u4e00-\u9fa5]+')
rst2 = p4.findall(title)
print(rst2)

#贪婪和非贪婪
#贪婪：尽可能多的匹配，*表示贪婪匹配
#非贪婪：找到符合条件的最小内容即可，？表示非贪婪
#正则默认使用贪婪匹配

title1 = u'<div>name</div><div>age</div>'

p5 = re.compile(r'<div>.*</div>')
p6 = re.compile(r'<div>.*?</div>')

m3 = p5.search(title1)
print(m3.group())
m4 = p6.search(title1)
print(m4)