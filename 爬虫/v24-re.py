"""
python中正则模块是re
使用大致步骤：
1.compile函数将正则表达式的字符串变为一个Pattern对象
2.通过Pattern对象的一系列方法对文本进行匹配，匹配结果是一个Match对象
3.用Match对象的方法，对结果进行操纵
"""
import re

#\d表示数字，+表示前面内容至少出现了一次
s = r"\d+"#r表示后面是原生字符串，后面不需要转义

pattern = re.compile(s)

#返回一个Match对象
m = pattern.match('one12two2three3')
print(type(m))
#尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(m)

#后面两个参数是位置参数，表示查找范围
m1 = pattern.match('one12two2three3', 3, 10)
print(type(m1))
#默认匹配从头部开始查找，所以此次结果为None
print(m1)

print(m1.group())
print(m1.start())
print(m1.end())
print(m1.span())