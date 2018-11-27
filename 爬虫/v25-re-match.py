"""
正则结果Match的使用案例
"""

import re

#以下正则分成了两个组，以小括号为单位
s = r"([a-z]+) ([a-z]+)"
pattern = re.compile(s, re.I)   #s.I表示忽略大小写
m = pattern.match("Hello world wide web")

print(m)

#group(0)表示返回匹配成功的整个子串
m0 = m.group(0)
print(m0)

a0 = m.span(0) #返回匹配成功的整个子串的跨度
print(a0)

#group(1)表示返回的匹配成功第一个分组子串
m1 = m.group(1)
print(m1)
a1 = m.span(1)
print(a1)

m2 = m.group(2)
print(m2)
a2 = m.span(2)
print(a2)

ms = m.groups() #把所有分组打印出来
print(ms)
sa = m.span()
print(sa)
